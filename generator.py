import csv
import random
import time
import os

LOG_FILE = "logs/live_logs.csv"

os.makedirs("logs", exist_ok=True)

headers = [
    "failed_logins",
    "login_hour",
    "data_transferred_mb",
    "unique_ports_accessed"
]

if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)

print("Generating live SOC logs... Press CTRL + C to stop.")

while True:
    # Mostly normal traffic
    if random.random() < 0.75:
        row = [
            random.randint(0, 4),
            random.randint(8, 18),
            random.randint(20, 100),
            random.randint(1, 5)
        ]
    # Suspicious traffic
    else:
        row = [
            random.randint(15, 35),
            random.randint(0, 4),
            random.randint(700, 1500),
            random.randint(30, 80)
        ]

    with open(LOG_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(row)

    print(f"New log added: {row}")
    time.sleep(2)
