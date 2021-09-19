#Create a class with name EmployeeModel with 5
#properties EmpId int, EmpName string, EmailId string, Salary 
#float, IsEmployeeActive bool

#Create an object for the above EmployeeModel and assign the values to all 
#properties and print each property on console

#Create another object for the above EmployeeModel and assign different values to 
#all properties and print each property on console


class EmployeeModel:
    def  __init__(self,EmpId,EmpName,EmailId,Salary,IsEmployeeActive):
        self.EmpId=EmpId
        self.EmpName=EmpName
        self.EmailId=EmailId
        self.Salary=Salary
        self.IsEmployeeActive=IsEmployeeActive

    def myfunc(self):
        print("EmpId:",self.EmpId)
        print("EmpName:",self.EmpName)
        print("EmailId:",self.EmailId)
        print("Salary:",self.Salary)
        print("IsEmployeeActive:",self.IsEmployeeActive)
    
Employee1=EmployeeModel(982780,"Jayatheertha","jayatheerthagk@gmail.com",25000.00,"True")
Employee1.myfunc()

Employee2=EmployeeModel(982781,"Test","test.test@gmail.com",29000.00,"False")
Employee2.myfunc()
  
