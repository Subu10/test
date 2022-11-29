#Write a Program to take 3 digit number from user and print addition of its digits
#For example if user entered 352 number then output will be 10(Addition of all digits)
a=int(input("enter the three digit number"))
b=a//100
c=a%100
print("first digit is",b)
d=c//10
print("second digit is",d)
e=c%10
print("third digit is",e)
f=b+d+e
print("addition of three digits is",f)
