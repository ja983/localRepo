#instance method

class DecoratorExample:
    def __init__(self):
        print("Hello, Sir/Madam!")
        self.name="Jayatheertha"
    def example_function(self):
        print('I\'m a Fresher!')
        print('My name is ' + self.name)

de=DecoratorExample()
de.example_function()



