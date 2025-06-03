import os 
import requests
import urllib.parse
import http.client
from dotenv import load_dotenv

load_dotenv()
access_token = os.getenv("ACCESS_TOKEN")
app_code = os.getenv("THREADS_APP_CODE")

if access_token is None or app_code is None:
    # print("Please set the ACCESS_TOKEN and THREADS_APP_CODE environment variables.")
    exit(1) 

host = "graph.threads.net"
endpoint = "/v1.0/me/threads"
params = {
    'fields': "id,name",
    'access_token': access_token,
    'media_type': "text",
    'text': "Hello World",
}
url = f"{endpoint}?{urllib.parse.urlencode(params)}"

conn = http.client.HTTPSConnection(host)
conn.request("POST", url)

response = conn.getresponse()

body = response.read().decode()
print(body)

conn.close()

# response = requests.post(url=url,params=params)
# print("Status Code:", response.status_code)
# # print("Response Headers:", response.headers)
# print("Response Text:", response.text)

# if response.status_code == 200:
#     data = response.json()
#     post_id = data.get("id")
#     print("✅ Post Published! Post ID:", post_id)
#     print(f"🔗 View it at: https://www.threads.net/jongi85523/post/{post_id}")
#     print("User Name",data.get("name"))
# else:
#     print(f"resuqest failed with status code {response.status_code}")
#     print('Response:', response.text)