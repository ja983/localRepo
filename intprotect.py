#program on protected access modifier using one method

class Value:

    _valueofx=None

    def __init__(self,valueofx):
        self._valueofx=valueofx

    def _displayValueOfX(self):
        print(self._valueofx)

class Jala(Value):

    def __init__(self,valueofx):
        Value.__init__(self,valueofx)

    def displayValue(self):

        print("Value of x:",self._valueofx)

obj=Jala(10)

obj.displayValue()

