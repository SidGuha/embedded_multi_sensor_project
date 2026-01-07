#include "DHT.h"

#define DHTPIN 27
#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  delay(500);
  dht.begin();
  Serial.println("timestamp_ms,temp_c,humidity_pct");
}

void loop() {
  float h = dht.readHumidity();
  float t = dht.readTemperature(); // Celsius

  if (isnan(h) || isnan(t)) {
    Serial.println("ERR,NaN,NaN");
  } else {
    Serial.print(millis());
    Serial.print(",");
    Serial.print(t, 2);
    Serial.print(",");
    Serial.println(h, 2);
  }

  delay(2000); 
}
