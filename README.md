# 🧠 User Behavior Anomaly Detection Dashboard

A real-time dashboard for detecting anomalous user behavior based on login activity, session patterns, and IP address changes. Built using **React**, **Flask**, **MongoDB**, and an **Isolation Forest** ML model.


<img width="564" alt="1" src="https://github.com/user-attachments/assets/0494e62b-9563-4f3d-95bd-f41d3255350c" />


## 🚀 Features

- 📥 Real-time log simulation and ingestion
- 🧠 Unsupervised anomaly detection using Isolation Forest
- 📊 Interactive dashboard with anomaly flags (✅ / ⚠️)
- 🧩 Modular code structure for easy integration and scaling
- 📦 MongoDB NoSQL backend for fast and flexible storage

---

## 🛠️ Tech Stack

| Layer        | Technology                          |
|--------------|--------------------------------------|
| Frontend     | React.js, Axios                      |
| Backend API  | Flask, Flask-CORS                    |
| ML Model     | Scikit-learn (Isolation Forest)      |
| Database     | MongoDB (local or cloud via Atlas)   |
| Other Tools  | Python, Requests, Pandas, NumPy      |

---

## 🧬 How It Works

### 1️⃣ Log Generation
A script `generate_live_logs.py` simulates login activity with randomized:
- `user_id`
- `IP`
- `Device`
- `Login Count`
- `Session Duration`
- `IP Change Count`

Logs are POSTed to the backend every few seconds.

### 2️⃣ Anomaly Detection
Backend uses an **Isolation Forest** ML model to:
- Analyze the log
- Label it as anomalous (`True`) or normal (`False`)
- Store it in MongoDB with the label

### 3️⃣ Frontend Dashboard
The React frontend:
- Fetches logs via `GET /api/logs`
- Displays them in a table
- Highlights anomalies using icons and colors (✔️/⚠️)

---

## 📂 Project Structure

