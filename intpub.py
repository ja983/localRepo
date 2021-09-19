# program to show the use of public Access Modifier

class Student:
    def __init__(self,id,name):
        self.studentid=id
        self.studentName=name 

    def displayId(self):
      print("Id: ",obj.studentid)

obj=Student(101,"Santhi")

print("Name: ",obj.studentName)

obj.displayId()
