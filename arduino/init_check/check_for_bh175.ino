#include <Wire.h>

void setup() {
  Serial.begin(115200);
  delay(500);
  Wire.begin(21, 22);

  Serial.println("I2C scan starting...");
}

void loop() {
  byte count = 0;

  for (byte addr = 1; addr < 127; addr++) {
    Wire.beginTransmission(addr);
    if (Wire.endTransmission() == 0) {
      Serial.print("Found I2C device at 0x");
      if (addr < 16) Serial.print("0");
      Serial.println(addr, HEX);
      count++;
      delay(5);
    }
  }

  Serial.print("Done. Devices found: ");
  Serial.println(count);
  delay(3000);
}
