追蹤ApexLegends玩家的遊戲內狀態 並投放至discord

### 功能(Features)

   追蹤玩家目前選擇的角色,玩家名稱,以及玩家當前狀況(離線&大廳&比賽中),和經過時間 並將其顯示至discord的狀態欄
   
   tracking player selected legends,player name,ingame status and timing, then show at discord gaming status
   
   
   
   
   



### 設定方式(Set up)


   ### playerInfo.json


   請於 playerInfo.json 文件中設置以下參數 (please set up the parameters in file 'playerInfo.json' )

    playerName #限輸入Origin玩家名稱 (Origin platform only)
   
    APIKey #請至https://portal.apexlegendsapi.com/ 申請 (Go https://portal.apexlegendsapi.com/ to register)
   
    Languages: TW/EN #目前僅支援中文(TW)/英文(EN) (#Traditional Chinese(TW) or English(EN))
    

   ### Discord


    若無法顯示 請至設定->動態設定->活動狀態中 將遊戲Hexaov discord pre-relese test(預設)加入





### 成果圖

TW:
<a href="https://github.com/a3510377" style="border-radius:50%">
    <img width="300px" src="https://media.discordapp.net/attachments/872419914718273587/976852857506656256/unknown.png">
</a>

EN:
<a href="https://github.com/a3510377" style="border-radius:50%">
    <img width="300px" src="https://media.discordapp.net/attachments/872419914718273587/976855909185773578/unknown.png">
</a>


### Bugs
若無法正常開啟 請以管理員模式開啟主程式

目前無法檢測到靶場/競技場/rank地圖 因此已直接移除

若進入的組隊房間房主正在遊戲中,狀態藍也會顯示比賽中





