import pandas as pd
import joblib
import time
import os
from datetime import datetime

MODEL_FILE = "models/soc_anomaly_model.pkl"
LOG_FILE = "logs/live_logs.csv"
ALERT_FILE = "alerts/alerts.csv"

model = joblib.load(MODEL_FILE)

os.makedirs("alerts", exist_ok=True)

if not os.path.exists(ALERT_FILE):
    with open(ALERT_FILE, "w") as file:
        file.write(
            "timestamp,failed_logins,login_hour,data_transferred_mb,"
            "unique_ports_accessed,severity,status,action\n"
        )


def get_risk_level(row):
    score = 0

    if row["failed_logins"] > 20:
        score += 2
    elif row["failed_logins"] > 10:
        score += 1

    if row["data_transferred_mb"] > 1000:
        score += 2
    elif row["data_transferred_mb"] > 500:
        score += 1

    if row["unique_ports_accessed"] > 50:
        score += 2
    elif row["unique_ports_accessed"] > 20:
        score += 1

    if row["login_hour"] < 5:
        score += 1

    if score >= 5:
        return "CRITICAL"
    elif score >= 3:
        return "HIGH"
    elif score >= 2:
        return "MEDIUM"
    else:
        return "LOW"


print("SOC real-time monitor started... Press CTRL + C to stop.")

last_checked_row = 0
alert_count = 0
normal_count = 0

while True:
    if os.path.exists(LOG_FILE):
        logs = pd.read_csv(LOG_FILE)

        new_logs = logs.iloc[last_checked_row:]

        if not new_logs.empty:
            predictions = model.predict(new_logs)

            for position, (index, row) in enumerate(new_logs.iterrows()):
                risk_level = get_risk_level(row)

                if predictions[position] == -1:
                    alert_count += 1
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    action = "Investigate potential intrusion"

                    print("\n========== SECURITY ALERT ==========")
                    print(f"Timestamp: {timestamp}")
                    print(f"Severity: {risk_level}")
                    print(f"Failed Logins: {row['failed_logins']}")
                    print(f"Login Hour: {row['login_hour']}")
                    print(f"Data Transfer: {row['data_transferred_mb']} MB")
                    print(f"Ports Accessed: {row['unique_ports_accessed']}")
                    print(f"Action: {action}")
                    print(f"Total Alerts Detected: {alert_count}")
                    print("====================================\n")

                    with open(ALERT_FILE, "a") as file:
                        file.write(
                            f"{timestamp},{row['failed_logins']},{row['login_hour']},"
                            f"{row['data_transferred_mb']},{row['unique_ports_accessed']},"
                            f"{risk_level},ALERT,{action}\n"
                        )
                else:
                    normal_count += 1
                    print(f"[OK] Normal log checked - Row {index}")

            print("\n------ SOC MONITOR SUMMARY ------")
            print(f"Normal Logs Checked: {normal_count}")
            print(f"Alerts Detected: {alert_count}")
            print("---------------------------------\n")

            last_checked_row = len(logs)

    time.sleep(3)
