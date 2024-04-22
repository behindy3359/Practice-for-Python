print('키보드를 통해 쉼표(,)로 구분 된 상품 자료를 입력받아 조건에 맞게 가공한 후 출력하시오.')
#(지역코드,상품명,수량)을 입력받아 처리
def nameTOprice(name) :
    if name == '새우깡':
        return 450
    elif name == '감자깡':
        return 300
def codeTOregion(name) :
    if name == '100':
        return '강북'
    elif name == '200':
        return '강남'
def datainput() :
    dataRoom =[]
    while True:
        a = input('(지역코드,상품명,수량)을 입력해주세요 :')
        dataRoom.append(a)
        b = input('계속 입력하시겠습니까? (Y/N)')
        if b == 'y'or'Y':
            continue
        elif b == 'n'or'N' :
            break
    return dataRoom
def showTable(data) :
    print('지역  상품명   수량    단가    금액  ')
    for i in range(len(data)):
        oneStringData=str(data[i]).split(',')
        regionName=oneStringData[0]
        objectName=oneStringData[1]
        objectAmount=oneStringData[2]
        objectPrice=nameTOprice(objectName)
        allPrice=int(objectAmount)*objectPrice
        print('%s  %s   %s    %s    %s  '%(regionName, objectName, objectAmount, objectPrice, allPrice))

data=datainput()
showTable(data)


