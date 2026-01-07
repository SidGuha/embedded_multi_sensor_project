import csv
import time
from collections import deque
import matplotlib.pyplot as plt

CSV_PATH = "data/log.csv"
MAXPTS = 600          # how many points to show (~last minute if 100ms)
REFRESH_S = 0.25      # plot refresh rate

t_vals = deque(maxlen=MAXPTS)
lux_vals = deque(maxlen=MAXPTS)

plt.ion()
fig, ax = plt.subplots()

def read_last_rows(path, max_rows=MAXPTS):
    """Read CSV and return last max_rows of (t_ms, lux)."""
    rows = []
    with open(path, "r", newline="") as f:
        r = csv.reader(f)
        for row in r:
            if not row or row[0] == "timestamp_ms":
                continue
            if len(row) < 2:
                continue
            try:
                t = int(float(row[0]))
                lux = float(row[1])
            except ValueError:
                continue
            rows.append((t, lux))
    return rows[-max_rows:]

while True:
    try:
        data = read_last_rows(CSV_PATH, MAXPTS)

        t_vals.clear()
        lux_vals.clear()
        for t, lux in data:
            t_vals.append(t)
            lux_vals.append(lux)

        ax.clear()
        if len(t_vals) > 2:
            # Convert ms -> seconds relative to first point so axis isn't huge
            t0 = t_vals[0]
            t_sec = [(t - t0) / 1000.0 for t in t_vals]

            ax.plot(t_sec, list(lux_vals))
            ax.set_xlabel("time (s)")
            ax.set_ylabel("light (lux)")
            ax.set_title("BH1750 Live Light Level")

            # Auto-zoom Y with a little padding
            y_min = min(lux_vals)
            y_max = max(lux_vals)
            pad = max(1.0, 0.05 * (y_max - y_min))
            ax.set_ylim(y_min - pad, y_max + pad)

        else:
            ax.set_title("Waiting for data...")

        plt.pause(0.001)
        time.sleep(REFRESH_S)

    except FileNotFoundError:
        ax.clear()
        ax.set_title("Waiting for data/log.csv ...")
        plt.pause(0.5)
        time.sleep(0.5)
