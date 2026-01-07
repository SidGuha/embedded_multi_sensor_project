#include <Wire.h>
#include <BH1750.h>

BH1750 lightMeter;

void setup() {
  Serial.begin(115200);
  delay(500);

  Wire.begin(21, 22);

  if (!lightMeter.begin()) {
    Serial.println("BH1750 not found");
    while (1);
  }

  Serial.println("timestamp_ms,light_lux");
}

void loop() {
  unsigned long t = millis();
  float lux = lightMeter.readLightLevel();

  Serial.print(t);
  Serial.print(",");
  Serial.println(lux, 1);

  delay(500);
}
