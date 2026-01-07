import csv
import os
import time
import serial

PORT = "COM5"          # set to your actual COM port
BAUD = 115200
OUTFILE = os.path.join("data", "log.csv")

os.makedirs("data", exist_ok=True)

ser = serial.Serial(PORT, BAUD, timeout=2)
time.sleep(0.5)

print("Logging BH1750... Ctrl+C to stop")

with open(OUTFILE, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["timestamp_ms", "light_lux"])
    f.flush()

    while True:
        line = ser.readline().decode(errors="ignore").strip()
        if not line:
            continue

        parts = line.split(",")
        if len(parts) != 2:
            continue

        try:
            t = int(float(parts[0]))
            lux = float(parts[1])
        except ValueError:
            continue

        w.writerow([t, lux])
        f.flush()
        print(t, lux)
