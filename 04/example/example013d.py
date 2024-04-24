kor = 100

def abc():
    print('i`m function!')
class My:
    kor = 90
    def abc(celf):
        print('i`m method!')
    def show(celf):
        kor =88
        print(celf.kor)
        print(kor)
        
        celf.abc()
        abc()
obj=My()
obj.show()
        