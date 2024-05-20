#print the pattern
#num=int(input("Enter a number:")) #Enter a value for upto which value you want to see the pattern
x='' #introduced an empty string to concatenate two string values
y=0  # i want to convert the concatenated string value into a integer value. so before placing it inside loop, 
    #here is the initial value, y=0
for i in range(1,5+1): #skipping the zero as the initial value
    for j in range(i): #so it can print the same number (suppose 3) for the i (suppose 3) times
        x+=str(i) #concatenate the strings together as long as the loop continues
        y=int(x) #convert string to integer
    print(y) # print the string
    x='' #again bring back x into an empty string so that previous string value doesn't hamper our pattern
    print(" ") 
        

