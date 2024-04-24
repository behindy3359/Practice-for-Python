from abc import *

class AbstractClass(metaclass=ABCMeta):
    @abstractmethod
    def abcMethod(self):
        pass
    
    def normalMethod(self):
        print('추상클래스 내의 일반 메소드')
    
class Child1(AbstractClass):
    name = '난 Child1'
    def abcMethod(self):
        print('추상메소드를 Child1 에서 오버라이드 함')

c1 = Child1()
print(c1.name)

c1.abcMethod()
c1.normalMethod()

c3 = Child1
c3.abcMethod(c3)

class Child2(AbstractClass):
    def abcMethod(self):
        print('추상메소드를 Child2 에서 오버라이드 함')
    def normalMethod(self):
        print('추상클래스의 일반 메소드를 재 정의')
        
c2 = Child2
c2.abcMethod(c2)
c2.normalMethod(c2)


parent = c1
parent.abcMethod()
parent.normalMethod()

parent = c2
parent.abcMethod(parent)
parent.normalMethod(c2)