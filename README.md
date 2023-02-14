# 簡介
這個程式會讀取日誌檔案, 然後把最後一行(倒數第二行)當作訊息發到你自己指定的Line Official Channel

<img width="320" alt="image" src="https://user-images.githubusercontent.com/691289/216745596-b58c7538-1d53-482a-9d8d-33dccc80c115.jpeg">

# 更新日誌
 - v0.1: 單開exe
 - v0.2: 支援多開exe

# 設定方式 (一次性前置作業)
- 註冊一個Line的開發者帳號 (免費)
   https://developers.line.biz/console/
- 創立一個channel, 名字隨意
<img width="646" alt="image" src="https://user-images.githubusercontent.com/691289/216746064-d09b43c6-13bc-44a3-bbe8-5d7b99a97fdc.png">

- 再創一個provider,在basic setting裡面最下面記下自己的userID
<img width="882" alt="image" src="https://user-images.githubusercontent.com/691289/216745406-80541150-da37-4146-9a02-1ead2bb82102.png">

- 選 "Messaging API", 然後創一個 "Channel access token", 記錄一下不要跟人分享
<img width="585" alt="image" src="https://user-images.githubusercontent.com/691289/216746237-ccebd59d-8e87-49e2-8d10-4c03d6d38974.png">

# 執行方式 1 (使用exe, 不需要安裝額外的東西,直接可以用)
1. 下載 https://github.com/sunnyp1227/lineagem-line/raw/main/line-notify.rar
2. 將這個exe和config.txt放進你的資料夾的log裡面
3. 更改config.txt,將至少第一跟第二行換成你自己的在上面申請的

```
line-notify-config.txt有四行

改成您的channel_access_token
改成您的_channel_userID
1 #您想要收到通知的log, 如果需要多個log, 請用半形,分開不要有任何空格: ex: 1,2,3
10 #刷新頻率(秒), 避免被揍的時候連續收到通知

```

# 執行方式 2 (自行安裝python, pip, SDK)
- 安裝python, pip, 還有Line的SDK
https://www.python.org/downloads/
```
$ pip install line-bot-sdk
```

# 執行方式 
下載post-message.py, 更改裡面的

1. channel access token
2. userID
3. log

打開command line (windows key + r), 然後執行
```
python post-message.py
```
