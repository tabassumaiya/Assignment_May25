#Write a Python program that takes the coordinates (x, y) of
#a point as input and prints out which quadrant it belongs to (1st, 2nd, 3rd, or 4th).

x=int(input("Enter x: "))
y=int(input("Enter y: "))
if x==0 and y==0:
    print("Origin")
elif x>0 and y>0:
    print("1st Quadrant")
elif x>0 and y<0:
    print("4th Quadrant")
elif x<0 and y>0:
    print("2nd Quadrant")
else:
    print("3rd Quadrant")
