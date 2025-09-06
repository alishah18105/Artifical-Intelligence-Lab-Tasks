#Write a Python program to convert temperatures to and from celsius,
#Fahrenheit.
#Formula : c/5 = f-32/9
#Expected Output :
#Enter temp in Celsius: 60°C
#Temperature in Fahrenheit is :140

print("Enter temperature in Celsius:")
temp = float(input())

fahrenheit = (temp * 9/5) + 32
print(f"Temperature {temp}°C in Fahrenheit is: {fahrenheit}°F")