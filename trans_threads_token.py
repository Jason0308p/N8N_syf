import os
import requests
from dotenv import load_dotenv

load_dotenv()

short_token = os.getenv("THREADS_ACCESS_TOKEN")
app_secret = os.getenv("THREADS_APP_CODE")

if not short_token or not app_secret:
    print("❌ SHORT_TOKEN 或 APP_SECRET 沒有正確設置")
    exit(1)

url = "https://graph.threads.net/access_token"
params = {
    "grant_type": "th_exchange_token",
    "client_secret": app_secret,
    "access_token": short_token,
}

response = requests.get(url, params=params)

print("🔁 Response Status:", response.status_code)
print("📦 Response Text:", response.text)

try:
    data = response.json()
    if "access_token" in data:
        print("✅ 成功獲得 Long-Lived Token：")
        print(data["access_token"])
        print(f"⏳ 有效時間（秒）: {data.get('expires_in', '不明')}")
    else:
        print("⚠️ 回傳結果中沒有 access_token：")
        print(data)
except Exception as e:
    print("❌ JSON Decode 失敗，可能回傳不是 JSON：")
    print(e)
