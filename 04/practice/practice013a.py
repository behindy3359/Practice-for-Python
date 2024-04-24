from practice013b import *

class Machine:
    cupCount = 0
    
    def showData():
        coin = int(input('동전을 입력하세요'))
        cupCount = int(input('몇 잔을 원하세요'))
        re = CoinIn.calc(coin,cupCount)