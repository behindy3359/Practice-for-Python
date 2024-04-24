class Car:
    handle = 0
    speed = 0

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.abcdefg = speed
    
    def showData(self):
        km='킬로미터'
        msg='속도:'+str(self.abcdefg)+km
        return msg

car1 = Car('tom', 10)

print(car1.handle, car1.name, car1.speed, car1.abcdefg)
car1.color='검정'
print('car1.color:', car1.color)

car2 = Car('james',20)
print(car2.handle, car2.name, car2.speed, car2.abcdefg)

print(id(Car), id(car1), id(car2))
print('car1', car1.showData())
print('car2', car2.showData())

car1.speed=50
print('car1', car1.showData())

print('car1 속도:', car1.speed)
print('car2 속도:', car2.speed)