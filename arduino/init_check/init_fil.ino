const int ADC_PIN = 32;   
const int SAMPLE_MS = 200;

void setup() {
  Serial.begin(115200);
  delay(500);
  analogReadResolution(12);
  Serial.println("timestamp_ms,adc");
}

void loop() {
  Serial.print(millis());
  Serial.print(",");
  Serial.println(analogRead(ADC_PIN));
  delay(SAMPLE_MS);
}
