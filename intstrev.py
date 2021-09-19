#Program to Reverse a String without using Reverse function

my_string=input("Enter a string:")
str=""
for i in my_string:
    str=i+str
print("Reversed String:", str)