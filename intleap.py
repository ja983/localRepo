#program to find whether a given year is a leap year or not

year=int(input("Enter a year:"))
if((year%400==0) or (year%100!=0) and (year%4==0)):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")

