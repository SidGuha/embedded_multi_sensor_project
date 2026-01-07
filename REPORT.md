# Project Report: Embedded Sensor Data Acquisition & Visualization

## 1. Objective
The goal of this project was to design and implement a modular embedded sensing system capable of acquiring real-time data from multiple sensors using a microcontroller, transmitting the data over serial communication, and visualizing it live on a host machine.

The project emphasizes reliable sensor integration, clean data pipelines, and real-time monitoring—key requirements in embedded and systems engineering workflows.

---

## 2. System Overview
The system consists of:
- A microcontroller-based embedded layer for sensor interfacing and data acquisition
- A serial communication pipeline (UART over USB)
- A Python-based host application for real-time data parsing and visualization

Sensor readings are streamed continuously in a structured format and processed on the host side with minimal latency.

---

## 3. Hardware Components
- **Microcontroller:** Arduino-based development board  
- **Sensors:**
  - DHT22 (AM2302) – temperature and humidity sensing
  - BH1750 (GY-302) – ambient light intensity sensing (lux)
- **Interfaces:** Digital I/O, I2C, UART (USB serial)

---

## 4. Software Architecture
### Embedded Firmware
- Periodic polling of connected sensors
- Sensor abstraction for modularity and extensibility
- Formatted serial output for robust downstream parsing
- Timing control to ensure stable sampling rates

### Host-Side Software
- Python script for serial data ingestion
- Real-time parsing and validation of incoming data
- Live plotting of sensor values for monitoring and debugging
- Designed to be easily extended to support additional sensors

---

## 5. Results
- Successfully achieved stable, real-time streaming of environmental and optical sensor data
- Verified sensor readings through live plots and serial logs
- Demonstrated modularity by integrating multiple sensor types with minimal firmware changes
- System maintained consistent performance over extended runtime tests

---

## 6. Challenges & Learnings
- Handling timing and synchronization between sensor reads and serial transmission
- Ensuring robust serial parsing on the host side
- Managing library dependencies and embedded build configuration
- Gained hands-on experience with embedded debugging, data pipelines, and real-time visualization

---

## 7. Future Improvements
- Add additional sensors (e.g., IMU, gas sensors)
- Implement binary serial protocol for improved efficiency
- Log data to files for offline analysis
- Port firmware to ESP32 or Jetson-connected microcontrollers
- Integrate basic fault detection and sensor validation

---

## 8. Conclusion
This project demonstrates a complete embedded-to-host data pipeline, combining low-level firmware development with higher-level software tooling. It reflects real-world embedded systems practices, including modular design, real-time constraints, and cross-domain integration between hardware and software.
