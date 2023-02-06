# 3). Convert a number into binary and binary to number.


# binary to number

a = input("Enter a binary number: ")
a = int(a)
num1,i = 0,0
while a>0:
    b = a%10
    c = b*(2**i)
    a = a//10
    num1 = num1 + c
    i+=1
print("binary to number is: ",num1)
# number into binary

num=0
b=0
a=1
print("Enter any number :")
n = int(input())
while n>0:
    num=n%2
    b=b+num*a
    a=a*10
    n=int(n/2)
print("binary number is =",b)
