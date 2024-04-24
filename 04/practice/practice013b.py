class CoinIn :
    
    coin = 0
    change = 0
    
    def calc(coin, cupCount) :
        change = coin - (cupCount*200)
        re =''
        if change <0 :
            print('동전을 더 넣어주세요 ,  부족한 금액 [', change*(-1),']')
        else :
            print('커피',cupCount,'잔과 잔돈',change,'원')