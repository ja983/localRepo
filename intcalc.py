def add(x,y):
    return x+y
def multiply(x,y):
    return x*y

print("Select operation.")
print("1.Add")
print("2.Multiply")

while True:
    choice=input("Enter choice(1/2):")

    if choice in ('1','2'):
        a=float(input("Enter a:"))
        b=float(input("Enter b:"))

        if choice=='1':
            print(a,"+",b,"=",add(a,b))

        elif choice=='2':
            print(a,"*",b,"=",multiply(a,b))
        break
    else:
        print("Invalid Input")

