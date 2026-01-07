import csv
import serial
import time

PORT = "COM5"   
BAUD = 115200
OUTFILE = "data/log.csv"

ser = serial.Serial(PORT, BAUD, timeout=1)
time.sleep(2)

print("Logging... Ctrl+C to stop")

with open(OUTFILE, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["timestamp_ms", "adc"])

    while True:
        line = ser.readline().decode(errors="ignore").strip()
        if not line:
            continue

    
        parts = line.split(",")
        if len(parts) != 2:
            continue
        if not (parts[0].isdigit() and parts[1].isdigit()):
            continue

        w.writerow(parts)
        f.flush()
        print(parts)

