# 🚨 SOC Real-Time Monitoring System (Machine Learning)

A real-time Security Operations Center (SOC) monitoring system that simulates live network activity, detects anomalies using machine learning, assigns severity levels, and generates actionable security alerts.

---

## 🔍 Overview

This project demonstrates how machine learning can be integrated into SOC workflows to detect suspicious network behavior in real-time.

The system continuously:
- Generates simulated network logs
- Monitors incoming activity
- Detects anomalies using an ML model
- Assigns severity levels (LOW → CRITICAL)
- Produces analyst-style alerts
- Stores alerts for further investigation

---

## 🧠 Architecture


---

## ⚙️ Features

- 📡 Real-time log generation (simulated network activity)
- 🤖 Machine learning anomaly detection (Isolation Forest)
- 🚨 Severity classification (LOW, MEDIUM, HIGH, CRITICAL)
- 📊 Analyst-style alert output
- 📁 Alert persistence (CSV storage)
- 🔁 Continuous monitoring loop

---

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- Joblib
- CSV-based logging

---

## 📂 Project Structure
soc-realtime-monitor/
├── generator.py # Simulates live network activity
├── monitor.py # Real-time anomaly detection engine
├── logs/
│ └── live_logs.csv # Generated logs
├── models/
│ └── soc_anomaly_model.pkl # Trained ML model
├── alerts/
│ └── alerts.csv # Detected alerts
├── README.md


---

## 🚀 How to Run

### 1️⃣ Activate environment

```bash
source ~/projects/ml_env/bin/activate


2️⃣ Start log generator
python generator.py

3️⃣ Start real-time monitor (new terminal)
python monitor.py

🧪 Sample Output
========== SECURITY ALERT ==========
Timestamp: 2026-04-25 23:33:18
Severity: CRITICAL
Failed Logins: 33
Login Hour: 3
Data Transfer: 1097 MB
Ports Accessed: 35
Action: Investigate potential intrusion
====================================

🧠 Detection Logic
The system uses:


Isolation Forest for anomaly detection


Rule-based scoring for severity classification


Risk Factors:


High failed login attempts


Unusual login hours (late night)


Large data transfers


High number of ports accessed



📈 Use Cases


SOC analyst training simulations


Threat detection prototyping


Security monitoring demonstrations


ML + cybersecurity portfolio projects



⚠️ Limitations


Uses simulated data (not production logs)


No external SIEM integration (e.g., Splunk)


Basic ML model (can be improved with more data)



🔮 Future Improvements


Integration with real log sources (e.g., syslog, auth.log)


Web dashboard for live monitoring


Email/SMS alerting


Advanced ML models


SIEM integration (Splunk / ELK)



👤 Author
Dunsin Fakorede
Cybersecurity | Machine Learning | Project Management

⭐ If you find this useful
Give this repo a star and connect!

