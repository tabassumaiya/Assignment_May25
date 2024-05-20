#Write a Python program that takes an integer input from the user
#and calculates the sum of its digits using a while loop.

user_input=int(input("Enter a number: "))
num=user_input
sum=0
while num!=0:
    sum+=num%10
    num//=10
print("The sum of the digits of",user_input,"is",sum)