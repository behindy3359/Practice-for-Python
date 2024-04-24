class TestClass:
    aa = 1
    def __init__(a) :
        print('생성자')
    def __del__(b) :
        pass
    def printMEssage(c) :
        name ='한국인'
        print(name,' ',c.aa)

print(TestClass.aa)
test=TestClass()
print(test.aa)

test.printMEssage()
TestClass.printMEssage(test)
print('클래스 타입', isinstance(test, TestClass))