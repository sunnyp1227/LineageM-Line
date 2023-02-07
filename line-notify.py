from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError
import time
import os

def read_file_lines(file_path):
    with open(file_path, 'r') as file:
        one = file.readline().strip()
        two = file.readline().strip()
        three = file.readline().strip()
        four = file.readline().strip()
        return one, two, three, four

print('歡迎使用天堂M六區-死亡騎士一位工程師玩家寫的小工具')
print('Ver: 0.2 程式碼和使用教學: https://github.com/sunnyp1227/lineagem-line')

config_path = r".\line-notify-config.txt"
channel_access_token, channel_user_id, log_numbers, refresh_cadence_in_seconds = read_file_lines(config_path)
line_bot_api = LineBotApi(channel_access_token)

log_modification_times = {}

while True:
    for log_number in log_numbers.split(','):
        log_path =r'.\{}.log'.format(log_number)
        current_modification_time = int(os.stat(log_path).st_mtime)
        if log_number in log_modification_times:
            last_modification_time = log_modification_times[log_number]
            if current_modification_time > last_modification_time:
                log_modification_times[log_number] = current_modification_time
                with open(log_path, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                    last_line = '[Log {}] '.format(log_number) + lines[-2][1:].strip()
                    try:
                        line_bot_api.push_message(channel_user_id, TextSendMessage(text=last_line))
                        print(last_line)
                    except LineBotApiError as e:
                        # error handle
                        print('line的設置可能有問題')
                        print(e)
        else:
            log_modification_times[log_number] = current_modification_time
    time.sleep(int(refresh_cadence_in_seconds))
