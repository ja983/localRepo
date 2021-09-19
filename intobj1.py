#create multiple objects in one class

class MyClass:
    variable='Dog'

    def function(self):
        print("This is a message inside the class.")

myobjectx=MyClass()
myobjecty=MyClass()

myobjecty.variable='barking'

print(myobjectx.variable)
print(myobjecty.variable)

