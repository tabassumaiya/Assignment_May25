#Write a Python program that takes an integer input from the
#user and prints its reverse using a while loop.
User_input=int(input("Enter a number: "))
num=User_input
x=''
while num!=0:
    x+=str(num%10)
    num=num//10
print("The reverse of",User_input,"is",int(x))
"""
Alternate way to solve:
num=int(input("Enter a number: ))
num1=str(num)
digit=len(num1)
x=''
while digit!=0:
    digit=digit-1
    x+=num1[digit]
print("The reverse of",num,"is",int(x))
"""
