# 簡介
這個程式會讀取日誌檔案, 然後把最後一行(倒數第二行)當作訊息發到你自己指定的Line Official Channel

<img width="240" alt="image" src="https://user-images.githubusercontent.com/691289/216745596-b58c7538-1d53-482a-9d8d-33dccc80c115.jpeg">

# 更新日誌
 - v0.1: 單開exe
 - v0.2: 支援多開exe

# 設定方式 (一次性前置作業)
| 步驟      | 說明          | 截圖 |
| ------------- |:-------------|:-----|
| 1      | 使用你自己的line去登入並註冊一個Line的business ID (免費) | https://developers.line.biz/console/|
| 1.1      | 選上面那個登入 | <img width="240" alt="Screenshot 2023-04-20 at 2 26 46 AM" src="https://user-images.githubusercontent.com/691289/233322886-51e32857-65e1-4e0f-bd4c-54e6255f87c5.png">|
| 2      | 創一個provider | <img width="1249" alt="Screenshot 2023-04-20 at 2 31 25 AM" src="https://user-images.githubusercontent.com/691289/233324396-2b4b1192-b855-456d-b478-e597edeec247.png">|
| 2.2      | Provider的名字隨意取 | <img width="635" alt="Screenshot 2023-04-20 at 2 31 51 AM" src="https://user-images.githubusercontent.com/691289/233324475-92fa0a6a-94f9-4b23-a77e-fed94cc76b42.png">|
 | 3     | 點選+ "create a new channel" 來創立一個channel, 名字隨意. 這個頻道名會是之後你接收訊息的頻道名稱 | <img width="646" alt="image" src="https://user-images.githubusercontent.com/691289/216746064-d09b43c6-13bc-44a3-bbe8-5d7b99a97fdc.png">|    
 | 3.1     | 選左邊第二個messaging API | <img width="808" alt="Screenshot 2023-04-20 at 2 43 03 AM" src="https://user-images.githubusercontent.com/691289/233327321-a53f436b-00c2-402d-bf76-50f9892bf45a.png">|    
 | 3.2     | 把所有格子填完,最主要的是頻道名稱 | <img width="474" alt="Screenshot 2023-04-20 at 2 48 26 AM" src="https://user-images.githubusercontent.com/691289/233329259-db761d36-3c57-402b-8308-1226f940ed6d.png">|    
 | 4     | 完成以上步驟之後應該可以看到你自己的頻道 | <img width="882" alt="image" src="https://user-images.githubusercontent.com/691289/216745406-80541150-da37-4146-9a02-1ead2bb82102.png">|
 | 5     | 去basic setting, 最下面記下自己的userID | <img width="882" alt="image" src="https://user-images.githubusercontent.com/691289/216745406-80541150-da37-4146-9a02-1ead2bb82102.png">|  
 | 5.1     | 選 "Messaging API", 然後創一個 "Channel access token", 複製下來不要跟人分享 | <img width="585" alt="image" src="https://user-images.githubusercontent.com/691289/216746237-ccebd59d-8e87-49e2-8d10-4c03d6d38974.png"> |
  | 5.2     | 用你自己的手機line掃描 "Messaging API" 裡面的QR Code來加你剛才創的頻道好友| <img width="450" alt="Screenshot 2023-04-20 at 2 54 22 AM" src="https://user-images.githubusercontent.com/691289/233330972-19986f8a-fa21-42ff-a2da-114cae3d1c5a.png">
 
# 執行方式 1 (使用exe, 不需要安裝額外的東西,直接可以用)
1. 下載 https://github.com/sunnyp1227/lineagem-line/raw/main/line-notify.rar
2. 將這個exe和config.txt放進你的大尾資料夾的log資料夾裡面
3. 用記事本打開line-notify-config.txt,將

| 步驟      | 說明          |
| -------------|:-------------|
|第一行 | 替換成5.1步驟的channel access token|
|第二行 | 跟第二行換成設定步驟5的user ID|
```
line-notify-config.txt有四行

改成您的channel_access_token
改成您的_channel_userID
1 #您想要收到通知的log, 如果需要多個log, 請用半形,分開不要有任何空格: ex: 1,2,3
10 #刷新頻率(秒), 避免被揍的時候連續收到通知

```
4. 打開line-notify.exe執行即可


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
