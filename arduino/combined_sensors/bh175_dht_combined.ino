#include <Wire.h>
#include <BH1750.h>
#include "DHT.h"

#define DHTPIN 27
#define DHTTYPE DHT22

BH1750 lightMeter;
DHT dht(DHTPIN, DHTTYPE);

// DHT22 should be read ~every 2 seconds
const unsigned long DHT_PERIOD_MS = 2000;
unsigned long lastDhtMs = 0;
float lastTemp = NAN;
float lastHum = NAN;

void setup() {
  Serial.begin(115200);
  delay(300);

  Wire.begin(21, 22);

  if (!lightMeter.begin(BH1750::CONTINUOUS_HIGH_RES_MODE)) {
    Serial.println("BH1750 not found");
    while (1);
  }

  dht.begin();

  Serial.println("timestamp_ms,light_lux,temp_c,humidity_pct");
}

void loop() {
  unsigned long t = millis();

  // Read BH1750 whenever (fast)
  float lux = lightMeter.readLightLevel();

  // Read DHT22 only every 2 seconds
  if (t - lastDhtMs >= DHT_PERIOD_MS) {
    lastDhtMs = t;
    float h = dht.readHumidity();
    float temp = dht.readTemperature();

    if (!isnan(h) && !isnan(temp)) {
      lastTemp = temp;
      lastHum = h;
    }
  }

  // If DHT hasn't produced a reading yet, output -999 placeholders
  float outTemp = isnan(lastTemp) ? -999 : lastTemp;
  float outHum  = isnan(lastHum)  ? -999 : lastHum;

  Serial.print(t); Serial.print(",");
  Serial.print(lux, 1); Serial.print(",");
  Serial.print(outTemp, 2); Serial.print(",");
  Serial.println(outHum, 2);

  delay(200); // 5 Hz overall logging (nice for plotting)
}
