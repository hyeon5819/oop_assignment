class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print('울음소리 오버라이딩 합시다')


class Dog(Animal):
    def speak(self):
        print('멍멍!')


class Cat(Animal):
    def speak(self):
        print('냐옹!')


mydog = Dog('바둑이', 2)
print(mydog.name)
print(mydog.age)
mydog.speak()

mycat = Cat('나비', 3)
print(mycat.name)
print(mycat.age)
mycat.speak()
