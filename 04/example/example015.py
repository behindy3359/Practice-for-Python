from abc import *

class Employee(metaclass=ABCMeta):
    
    def __init__(a, irum, nai):
        a.irum = irum
        a.nai = nai
        
    @abstractmethod
    def pay(self) :
        pass
    
    @abstractmethod
    def data_print(self) :
        pass
    
    def irumnai_print(self) :
        print('이름:'+self.irum+', 나이:' + str(self.nai), end='')
    
class Temporary(Employee) :
    
    def __init__(a, irum, nai, ilsu, ildang):
        Employee.__init__(a, irum, nai)
        a.ilsu = ilsu
        a.ildang = ildang
    
    def pay(a):
        return a.ilsu*a.ildang
    
    def data_print(b):
        b.irumnai_print()
        print(',월급 :' +str(b.pay()))
        
class Regular(Employee) :
    
    def __init__(a, irum, nai, salary):
        super().__init__(irum, nai)
        a.salary = salary    
    
    def pay(a):
        return a.salary
    
    def data_print(b):
        b.irumnai_print()
        print(',급여 :' +str(b.pay()))

t = Temporary('홍길동', 25, 20, 150000)
r = Regular('한국인', 27, 3500000)

t.data_print()
r.data_print()
     