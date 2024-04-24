class Dog:
    kind='canine'
    def __init__(self, name) :
        self.name = name
dog1 = Dog('shepard')
dog2 = Dog('SiberianHusky')
dog3 = Dog()


print(dog1.kind)
print(dog2.kind)
print(dog3.kind)
print(dog1.name)
print(dog2.name)
print(dog3.name)