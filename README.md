# ESP32 Multi-Sensor Data Logger (BH1750 + DHT22)

An ESP32-based embedded sensing and telemetry system that acquires real-time environmental data, streams it over serial, logs it to disk, and visualizes it live on a host machine.

This project demonstrates end-to-end **embedded firmware + host-side tooling**, suitable for IoT, edge computing, and embedded systems applications.

---

## Features
- Real-time data acquisition on ESP32
- Multi-sensor integration using I²C and GPIO
- Structured CSV telemetry over UART
- Python-based logging and live visualization
- Modular firmware and host tooling

---

## Sensors
- **BH1750 (GY-302)** – Ambient light sensor (lux) over I²C  
- **DHT22 / AM2302** – Temperature (°C) and humidity (%) sensor over GPIO  

---

## Tech Stack
- **Firmware:** ESP32, Arduino, C/C++
- **Protocols:** I²C, UART, GPIO
- **Host Tools:** Python, pySerial, Matplotlib
- **Data Format:** CSV

---

## Hardware Setup

### ESP32 Wiring

#### BH1750 (I²C)
- VCC → 3.3V  
- GND → GND  
- SDA → GPIO 21  
- SCL → GPIO 22  

#### DHT22 Module
- `+` → 3.3V  
- middle pin (signal) → GPIO 27  
- `-` → GND  

> ⚠️ Use **3.3V only**. Close Arduino Serial Monitor before running Python scripts.

---

## Firmware (Arduino)

Available sketches:
- `arduino/bh1750_only/bh1750_only.ino`
- `arduino/dht22_only/dht22_only.ino`
- `arduino/combined_bh1750_dht22/combined_bh1750_dht22.ino` **(recommended)**

The combined firmware outputs structured CSV over serial:

timestamp_ms,light_lux,temp_c,humidity_pct

Baud rate: **115200**

---

## Host Setup (Python)

### Install dependencies and run terminals
```bash
pip install -r requirements.txt
```

## Run Logger(Terminal 1)-Sample
```bash
python python/log_serial.py
```

## Run Live Plotter(Terminal 2)-Sample
```bash
python python/live_plot.py
```
