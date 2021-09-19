#program on illustrating the read-only property by taking as class Employee

class employee:
    def __init__(self,name,position):
        self.name=name
        self.position=position

    @property
    def employeeid(self):
        return "employee's identification is {},{}".format(self.name,self.position)

employee1=employee("Jayatheertha","Web Developer")
print(employee1.employeeid)
