class TestClass:
    aa=1
    def __init__(self):
        print('생성자')
    def __del__(self):
        pass
    
    def printMessage(self):
        name='한국인'
        print(name,'',self.aa)

print(TestClass.aa)
test=TestClass()
print(test.aa)


######
test.printMessage()
TestClass.printMessage(test)
print('클래스 타입:',isinstance(test, TestClass))