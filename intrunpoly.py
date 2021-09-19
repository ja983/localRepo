#runtime polymorphism

class Animal:
    def makeNoise(self):
        raise NotImplementedError

class Cat(Animal):
    def makeNoise(self):
        print("Meoooowwww")

class Dog(Animal):
    def makeNoise(self):
        print("Woooofffff")

a=Cat()
a.makeNoise()

a=Dog()
a.makeNoise()
