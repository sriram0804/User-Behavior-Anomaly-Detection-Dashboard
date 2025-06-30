import requests
import random
import time

API_URL = "http://localhost:5000/api/logs"

def generate_random_log():
    user_id = f"user_{random.randint(1, 50)}"
    ip = f"192.168.0.{random.randint(1, 255)}"
    device = random.choice(["Chrome", "Firefox", "Edge", "Safari", "Opera"])
    login_count = random.randint(1, 20)
    avg_session_duration = round(random.uniform(5, 100), 2)
    ip_change_count = random.randint(0, 6)

    return {
        "user_id": user_id,
        "ip": ip,
        "device": device,
        "features": {
            "login_count": login_count,
            "avg_session_duration": avg_session_duration,
            "ip_change_count": ip_change_count
        }
    }

def send_logs(count=20, delay=0.5):
    for i in range(count):
        log = generate_random_log()
        try:
            response = requests.post(
                API_URL,
                json=log,
                headers={"Content-Type": "application/json"}
            )

            # Handle non-JSON or error response
            try:
                anomaly_status = response.json().get('anomaly', 'Unknown')
                print(f"[{i+1}/{count}] ✅ Sent log for {log['user_id']} → Anomaly: {anomaly_status}")
            except Exception as json_err:
                print(f"[{i+1}/{count}] ❌ Invalid JSON response: {response.text}")

        except requests.exceptions.RequestException as e:
            print(f"[{i+1}/{count}] ❌ Request failed: {e}")

        time.sleep(delay)

if __name__ == "__main__":
    send_logs(count=20, delay=0.5)
