#Write a Python program that takes a person's age as input and
#prints out whether they are an infant (0-1), toddler (1-3), child (4-12), teenager
#(13-19), adult (20+).
age=int(input("Enter age: "))
if age>=20:
    print("Adult")
elif age>=13:
    print("Teenager")
elif age>=4:
    print("Child")
elif age>=1:
    print("Toddler")
else:
    print("Infant")