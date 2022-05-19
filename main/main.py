# -*- coding: utf-8 -*-


import sys
import time
from pypresence import Presence
from PyQt5 import QtCore, QtGui, QtWidgets
import asyncio
import json
import requests
import os
class Ui_MainWindow(object):
    id = ''
    details = ''
    state = ''
    image = ''
    timer = 0
    RPC = None
    discord_status = False
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(250, 250)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_playerName = QtWidgets.QLabel(self.centralwidget)
        self.label_playerName.setGeometry(QtCore.QRect(10, 100, 240, 20))
        self.label_playerName.setObjectName("label_playerName")

        self.Button_start = QtWidgets.QPushButton(self.centralwidget)
        self.Button_start.setGeometry(QtCore.QRect(50, 150, 150, 30))
        self.Button_start.setObjectName("Button_start")

        MainWindow.setCentralWidget(self.centralwidget)

        
        self.retranslateUI(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

    def retranslateUI(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Hexaov discord pre-relese test", "Hexaov discord pre-relese test"))
        self.Button_start.setText(_translate("MainWindow", "開始"))
        with open('playerInfo.json', 'r', encoding = 'utf-8') as f:
            cfgDict=json.loads(f.read())
            self.PlayerName=cfgDict['playerName']
            self.APIKey=cfgDict['APIKey']
            self.Languages=cfgDict['Languages']
        self.setLanguageDict(self.Languages)

        self.label_playerName.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:400;\">玩家名稱 : %s</span></p></body></html>" % self.PlayerName))
    def setLanguageDict(self,Language): 
        LanguageMapDictEN={
            "Offline": "Offline",
            "offline": "offline",
            "InMatch": "in Match",
            "inMatch": "in Match",
            "inLobby": "in Lobby",
            "in Lobby": "in Lobby",

            "Ash": "Ash",
            "Bangalore": "Bangalore",
            "Bloodhound": "Bloodhound",
            "Caustic": "Caustic",
            "Crypto": "Crypto",
            "Fuse": "Fuse",
            "Gibraltar": "Gibraltar",
            "Horizon": "Horizon",
            "Lifeline": "Lifeline",
            "Loba": "Loba",
            "MadMaggie": "Mad Maggie",
            "Mirage": "Mirage",
            "Newcastle": "Newcastle",
            "Octane": "Octane",
            "Pathfinder": "Pathfinder",
            "Rampart": "Rampart",
            "Revenant": "Revenant",
            "Seer": "Seer",
			"Valkyrie": "Valkyrie",
			"Wattson": "Wattson",
            "Wraith": "Wraith",
            "Storm Point": "Storm Point",
			"Olympus": "Olympus",
			"World Edge": "World Edge"
            }
        LanguageMapDictTW={
            "Offline": "離線",
            "InMatch": "比賽中",
            "inMatch": "比賽中",
            "inLobby": "大廳",
            "offline": "離線",
            "Ash": "艾許",
            "Bangalore": "邦加羅爾",
            "Bloodhound": "尋血犬",
            "Caustic": "腐蝕",
            "Crypto": "暗碼士",
            "Fuse": "轟哥",
            "Gibraltar": "直布羅陀",
            "Horizon": "天際線",
            "Lifeline": "生命線",
            "Loba": "蘿芭",
            "MadMaggie": "瘋狂瑪吉",
            "Mirage": "幻象",
            "Newcastle": "紐卡索",
            "Octane": "辛烷",
            "Pathfinder": "探路者",
            "Rampart": "蕾帕特",
            "Revenant": "亡靈",
            "Seer": "席爾",
			"Valkyrie": "瓦爾基里",
			"Wattson": "華森",
            "Wraith": "惡靈",
            "Storm Point": "風暴點",
			"Olympus": "奧林匹斯",
			"World Edge": "世界邊緣"
            }
        if self.Languages in 'TW':
            self.LanguageMapDict=LanguageMapDictTW
        if self.Languages in 'EN':
            self.LanguageMapDict=LanguageMapDictEN

    def LanguageMapEN(self,name): 
        return self.LanguageMapDict[name]
    def LanguageMapTW(self,name): 
        return self.LanguageMapDict[name]

    def getUrlRaw(self,url):
        r5 = requests.get(url)
        return r5.text
    def getUidByName(self,playerName):
        player = playerName #一定要Origin
        PLATFORM='PC' 
        URL = "https://api.mozambiquehe.re/origin?auth="+ self.APIKey + "&player=" + player + "&platform=" + PLATFORM
        dictUID = json.loads(self.getUrlRaw(URL))
        return dictUID["uid"]


class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)

    def loopEvent(self):
        self.hide() #隱藏windows

        self.timer = int(time.time())
        self.id = '742751910401933432'
        self.details = 'Apex Legends'
        self.state = '讀取中'
        self.stateNew='讀取中'
        self.image = 'apex'

        self.RPC = Presence(client_id = self.id)
        self.RPC.connect()
        self.RPC.update(large_image = self.image, details =  self.details, state =  self.state, start = self.timer)
        while (1):

            UID = self.getUidByName(self.PlayerName)
            PLATFORM='PC' 
            URL = "https://api.mozambiquehe.re/bridge?auth=" +self.APIKey+"&uid=" + UID + "&platform=" + PLATFORM
            dictPlayerInfo = json.loads(self.getUrlRaw(URL))
            self.oldstate=dictPlayerInfo['realtime']['currentState']
            self.details=dictPlayerInfo['realtime']['selectedLegend'] #LOBA
            print(self.oldstate,self.stateNew , self.details)
            if self.oldstate in self.stateNew:
                pass
            else:
                self.timer=int(time.time())
            self.stateNew=dictPlayerInfo['realtime']['currentState'] #offline , In lobby , In match
            self.state=dictPlayerInfo['realtime']['currentState'] #offline , In lobby , In match
            if self.state in 'inMatch':
                self.state=self.LanguageMapTW(self.state)  #+' ('+self.LanguageMapTW(self.getMapName_MapTime()[0]) +')'
            else:
                self.state=self.LanguageMapTW(self.state)
            
            self.RPC.update(large_image=self.image, details=self.LanguageMapTW(self.details)+' ('+self.PlayerName+')', 
            state =  self.state, start = self.timer )
            asyncio.sleep(5) #5秒更新 
        



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    window.loopEvent()
    sys.exit(app.exec_())
    
    
