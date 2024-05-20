#Write a Python program that takes a temperature input
#in Celsius and converts it to Fahrenheit if the temperature is above 0°C, or to
#Kelvin if the temperature is below 0°C.

temp = float(input("Enter temperature in Celsius: "))
if temp > 0:
    result=((9*temp)/5)+32
    print("Temperature in Fahrenheit:",result)
else:
    result=(temp+273.15)
    print("Temperature in Kelvin:",result)