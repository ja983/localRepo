#using get & set accessories

class Vehicle:
    def __init__(self,value):
        self._value=value

    @property
    def value(self):
        print('Getting value')
        return self._value

    @value.setter
    def value(self,value):
        print('Setting value to '+value)
        self._value=value

x=Vehicle('Petrol')
print(x.value)

x.value='Diesel'
