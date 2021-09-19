#Define a static method and access that through a instance

class Shape:
    def info(msg):
        print(msg)
        print("This class is used for representing different shapes.")

Shape.info=staticmethod(Shape.info)
Shape.info('Welcome to Shape class')
