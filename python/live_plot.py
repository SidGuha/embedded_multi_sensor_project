import csv
import time
from collections import deque
import matplotlib.pyplot as plt

CSV_PATH = "data/log.csv"

xs = deque(maxlen=400)
ys = deque(maxlen=400)

plt.ion()
fig, ax = plt.subplots()

def read_rows():
    rows = []
    try:
        with open(CSV_PATH, "r", newline="") as f:
            r = csv.reader(f)
            for row in r:
                if not row or row[0] == "timestamp_ms":
                    continue
                if len(row) >= 2:
                    rows.append(row[:2])
    except FileNotFoundError:
        return []
    return rows

while True:
    rows = read_rows()[-400:]
    xs.clear(); ys.clear()

    for t, adc in rows:
        try:
            xs.append(int(t))
            ys.append(int(adc))
        except:
            pass

    ax.clear()
    if len(xs) > 2:
        ax.plot(xs, ys)
        ax.set_ylim(0, 4095)
    ax.set_title("ESP32 Live ADC (GPIO32)")
    ax.set_xlabel("timestamp_ms")
    ax.set_ylabel("adc ( (0..4095)")
    plt.pause(0.3)
    time.sleep(0.1)
