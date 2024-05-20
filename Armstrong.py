#Armstrong Number Checker: Write a Python program that takes an integer
#input from the user and checks if it is an Armstrong number (a number that is
#equal to the sum of its own digits raised to the power of the number of digits)
#using a for loop.
num=int(input("Enter a number: "))
num1=num #introducing a new variable "num1" to store the value "num", so "num" will not be modified after each iteration inside for loop
cnt=0   #here "cnt" is used to keep track of the number of digits in "num1". 
for i in range (num1,0,-1): #here iteration will be strated from num1 and will continue until num1 is reached to zero
    x=num1%10 #remainder of this operation is equal to the last digit
    cnt+=1 # at each iteration, cnt will be incremented by 1, will eventualy provide the number of digit after each iteration
    num1=num1//10  #floor division to remove the last digit.
    if num1==0 or num1<1: # breaking the operation so it doesn't continue infinitie 
        break
exp=cnt #assign the ultimate value of "cnt" which represents the total digit of the input number in a variable exp, 
         #which will be the exponent of next step
Current_number=0
num2=num #assign input number in a new variable num2, so the input number doesn
for i in range (exp): #run the loop equal times of its own number of digits
    x=num2%10    #seperating its each digit
    Current_number+=(x)**exp #sum of its own digits raised to the power of the number of digits
    num2=num2//10  #floor division to remove the last digit each time after each iteration.
if Current_number==num:
    print(num,"is an Armstrong number.")
else:
    print(num,"is not an Armstrong number")