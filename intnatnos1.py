#display n terms of odd natural numbers and their sum.

num=int(input("Enter terms of odd natural numbers:"))

sum=0
for num in range(num):
    if num%2!=0:
        print(num)
        sum+=num
print("The sum is",sum)
