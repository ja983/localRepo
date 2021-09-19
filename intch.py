#p program that takes a character as input and check the input (lowercase) is a vowel, a digit, or any other symbol. 
 

ch=input("Enter a character:")
if ch.lower() in "aeiou":
    print(ch,"is a lowercase vowel")
s=int(input("Enter a number:"))
for a in range(1,100):
    if s==a:
        print(s,"is a digit")

