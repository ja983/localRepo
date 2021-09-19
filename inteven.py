#program to print entered number of even numbers

max=int(input("Please maximium value:"))

for num in range(1,max+1):
    if(num%2==0):
        print("{0}".format(num))
