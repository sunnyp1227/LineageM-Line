from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

line_bot_api = LineBotApi('CHANGE-enter-your-channel-access-token')
channel_user_id = 'CHANGE-enter-your-user-ID'
log_path =r'''C:\Your-Log-Location\Log\1.log'''

last_modification_time = 0

while True:
    current_modification_time = int(os.stat(log_path).st_mtime)
    if current_modification_time > last_modification_time:
        last_modification_time = current_modification_time
        with open(log_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            last_line = lines[-2][1:].strip()
            try:
                line_bot_api.push_message(channel_user_id, TextSendMessage(text=last_line))
                print(last_line)
            except LineBotApiError as e:
                # error handle
                print(e)
    time.sleep(10)


