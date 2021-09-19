#create an object

class Car:
    color="green"
    maxSpeed="45kmph"

    def __init__(self,color,maxSpeed):
        self.color=color
        self.maxSpeed=maxSpeed

    def func(self):
        print("After calling func() method..")
        print("The car is",self.color,"in color.")
        print("It\'s maxSpeed is",self.maxSpeed)

myObj=Car('green','45kmph')
myObj.func()
