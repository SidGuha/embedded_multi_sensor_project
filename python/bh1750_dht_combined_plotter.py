import csv, time
from collections import deque
import matplotlib.pyplot as plt

CSV_PATH = "data/log.csv"
MAXPTS = 300
REFRESH_S = 0.5

plt.ion()
fig, ax = plt.subplots()

def read_csv():
    with open(CSV_PATH, "r", newline="") as f:
        r = csv.reader(f)
        rows = [row for row in r if row]
    return rows

while True:
    try:
        rows = read_csv()
        if len(rows) < 2:
            ax.clear()
            ax.set_title("Waiting for data...")
            plt.pause(0.1)
            time.sleep(REFRESH_S)
            continue

        header = rows[0]
        data_rows = rows[1:]

        # parse last MAXPTS rows
        data_rows = data_rows[-MAXPTS:]

        # build series
        t_ms = []
        series = {name: [] for name in header[1:]}

        for row in data_rows:
            if len(row) != len(header):
                continue
            try:
                t = float(row[0])
            except:
                continue

            t_ms.append(t)
            for i, name in enumerate(header[1:], start=1):
                try:
                    series[name].append(float(row[i]))
                except:
                    series[name].append(float("nan"))

        if len(t_ms) < 2:
            time.sleep(REFRESH_S)
            continue

        # Convert time to seconds relative
        t0 = t_ms[0]
        t_s = [(t - t0) / 1000.0 for t in t_ms]

        ax.clear()
        for name, vals in series.items():
            ax.plot(t_s, vals, label=name)

        ax.set_title("ESP32 Live Sensor Data")
        ax.set_xlabel("time (s)")
        ax.legend()
        plt.pause(0.1)
        time.sleep(REFRESH_S)

    except FileNotFoundError:
        ax.clear()
        ax.set_title("Waiting for data/log.csv ...")
        plt.pause(0.5)
        time.sleep(0.5)
