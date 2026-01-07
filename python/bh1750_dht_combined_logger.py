import os
import time
import serial

PORT = "COM5"   # change if needed
BAUD = 115200
OUTFILE = os.path.join("data", "log.csv")

os.makedirs("data", exist_ok=True)

ser = serial.Serial(PORT, BAUD, timeout=2)
time.sleep(0.5)

print(f"Logging multi-sensor CSV from {PORT} -> {OUTFILE} (Ctrl+C to stop)")

with open(OUTFILE, "w", newline="") as f:
    header_written = False

    while True:
        line = ser.readline().decode(errors="ignore").strip()
        if not line:
            continue

        # Skip boot noise
        if "," not in line:
            continue

        # Write header once (the ESP32 prints it)
        if line.startswith("timestamp_ms"):
            f.write(line + "\n")
            f.flush()
            header_written = True
            print("HEADER:", line)
            continue

        # Only start writing data after header
        if not header_written:
            continue

        f.write(line + "\n")
        f.flush()
        print(line)
