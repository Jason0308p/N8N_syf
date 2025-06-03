import os
import requests
from dotenv import load_dotenv

load_dotenv()

access_token = os.getenv("THREADS_ACCESS_TOKEN")

if not access_token:
    print("請先設定 ACCESS_TOKEN 環境變數")
    exit(1)

# 建立貼文草稿
def create_thread_draft(text):
    url = "https://graph.threads.net/v1.0/me/threads"
    params = {
        "access_token": access_token,
        "media_type": "TEXT",
        "text": "貼文2",
    }
    response = requests.post(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data.get("id")  # 授權發布草稿的臨時 ID
    else:
        print(f"建立貼文草稿失敗: {response.status_code} {response.text}")
        return None

# 發布貼文
def publish_thread(creation_id):
    url = "https://graph.threads.net/v1.0/me/threads_publish"
    params = {
        "access_token": access_token,
        "creation_id": creation_id,
    }
    response = requests.post(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data.get("id")  # 正式貼文的 id
    else:
        print(f"發布貼文失敗: {response.status_code} {response.text}")
        return None

if __name__ == "__main__":
    text = "Hello from Python script! 這是我的測試貼文。"
    print("正在建立貼文草稿...")
    creation_id = create_thread_draft(text)
    if creation_id:
        print(f"貼文草稿 ID: {creation_id}")
        print("正在發布貼文...")
        post_id = publish_thread(creation_id)
        if post_id:
            print(f"✅ 貼文發布成功！貼文 ID: {post_id}")
            print(f"貼文網址：https://www.threads.net/jongi85523/post/{post_id}")
        else:
            print("發布貼文失敗")
    else:
        print("建立貼文草稿失敗")
