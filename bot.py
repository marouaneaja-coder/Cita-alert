import os
import urllib.request
import urllib.parse
import json

TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

message = "✅ Cita Alert Bot is working! Telegram connected successfully."

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

data = urllib.parse.urlencode({
    "chat_id": CHAT_ID,
    "text": message
}).encode("utf-8")

request = urllib.request.Request(url, data=data)

with urllib.request.urlopen(request, timeout=20) as response:
    result = json.loads(response.read().decode("utf-8"))
    print(result)
