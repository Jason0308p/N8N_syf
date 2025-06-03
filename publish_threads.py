import os
# 可以直接使用 requests 套件，但這裡使用 http.client 來示範
# 這是 Python 內建的 HTTP 客戶端
import urllib.parse # for url encode
import http.client  # for HTTP requests

# load_dotenv 是 dotenv 套件的函式 
# 這個範例會從 .env 檔案讀取 ACCESS_TOKEN，並且把它載入到環境變數中
# 這樣就可以在程式中使用 os.getenv("ACCESS_TOKEN") 來取得 ACCESS_TOKEN
from dotenv import load_dotenv

load_dotenv()
access_token = os.getenv("LONG_LIVED_TOKEN")

if access_token is None:
    print("❌ 請先設定 ACCESS_TOKEN")
    exit(1)

# 你從建立草稿拿到的 creation_id，請替換
creation_id = "17899628391196597"

host = "graph.threads.net"
endpoint = "/v1.0/me/threads_publish"
params = {
    "access_token": access_token,
    "creation_id": creation_id,
}

url = f"{endpoint}?{urllib.parse.urlencode(params)}"

conn = http.client.HTTPSConnection(host)
conn.request("POST", url)

response = conn.getresponse()
body = response.read().decode()

print("🔁 Response Status:", response.status)
print("📦 Response Body:", body)

conn.close()
