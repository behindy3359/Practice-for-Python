def dofunc1():
    print('dofunc1() 호출')
def dofunc2(name):
    print('안녕 ',name,'좋은 아침이야')
def dofunc3(arg1, arg2):
    res=arg1+arg2
    return res
while True:
    a = int(input('1,2,3중 하나를 입력하시오'))
    if a==1:
        dofunc1()
    elif a==2:
        b = input('이름을 입력하시오!')
        dofunc2(b)
    elif a==3 :
        c=int(input('첫번째 숫자를 입력!'))
        d=int(input('두번째 숫자를 입력!'))
        print(dofunc3(c,d))
    else :
        break