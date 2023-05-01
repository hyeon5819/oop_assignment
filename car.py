class Car():
    def __init__(self, model, color, speed):
        self.model = model
        self.color = color
        self.speed = speed

    def accelerate(self):
        self.speed += 10

    def brake(self):
        self.speed -= 10

    def get_speed(self):
        print(self.speed)


mycar = Car('suv', 'red', 100)
print(mycar.model)
print(mycar.color)
print(mycar.speed)
mycar.accelerate()
mycar.get_speed()
mycar.brake()
mycar.get_speed()
