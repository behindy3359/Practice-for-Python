def machine ():
    coin = int(input('동전을 입력하세요 :'))
    cupCount = int(input('몇 잔을 원하세요 :'))
    
    change = coin-(200*cupCount)
    if change < 0 :
        print('동전을 더 넣어주세요')
    else :
        print('커피 ',cupCount,'잔과 잔돈',change,'원')

machine()