#. Write a Program to take 3 digit number from user and print its reverse number
# For example if user entered 352 number then output will be 253
a=int(input("enter three digit number"))
b=a//100
c=a%100
print("first digit is",b)
d=c//10
print("second digit is",d)
e=c%10
print("third digit is",e)
