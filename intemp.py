# Construct a class using any methods for employee details using its parameters

class employee:
    def __init__(self,first,last,sal):
        self.fname=first
        self.lname=last
        self.sal=sal
        self.email=first+'.'+last+'@gmail.com'

emp=employee('aayushi','johari',350000)
print("Employee Details")
print("First Name:",emp.fname)
print("Last Name:",emp.lname)
print("Salary:",emp.sal)
print(emp.email)

