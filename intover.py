#overloading class constructor

class  Fruits:
    def __init__(self,required_param,optional_param1=None,optional_param2=None):
        self.required_param=required_param
        self.optional_param1=optional_param1
        self.optional_param2=optional_param2

print(Fruits("apple").__dict__)
print(Fruits("apple","pear").__dict__)
print(Fruits("apple","pear","banana").__dict__)
