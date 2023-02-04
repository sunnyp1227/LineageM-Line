# 簡介
這個程式會讀取日誌檔案, 然後把最後一行(倒數第二行)當作訊息發到你自己指定的Line Official Channel

<img width="320" alt="image" src="https://user-images.githubusercontent.com/691289/216745596-b58c7538-1d53-482a-9d8d-33dccc80c115.jpeg">

# 設定方式
- 註冊一個Line的開發者帳號 (免費)
   https://developers.line.biz/console/
- 創立一個channel, 名字隨意
<img width="646" alt="image" src="https://user-images.githubusercontent.com/691289/216746064-d09b43c6-13bc-44a3-bbe8-5d7b99a97fdc.png">

- 再創一個provider,在basic setting裡面最下面記下自己的userID
<img width="882" alt="image" src="https://user-images.githubusercontent.com/691289/216745406-80541150-da37-4146-9a02-1ead2bb82102.png">

- 選 "Messaging API", 然後創一個 "Channel access token", 記錄一下不要跟人分享
<img width="585" alt="image" src="https://user-images.githubusercontent.com/691289/216746237-ccebd59d-8e87-49e2-8d10-4c03d6d38974.png">

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
