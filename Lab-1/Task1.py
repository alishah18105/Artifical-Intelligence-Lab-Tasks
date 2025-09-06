#Write a Python program to swap 4 variables values (input four values.
#Sample input:
#Before swapping
#a=2,b=56,c=78,d=9
#After Swapping
#a=,9,b=78,c=56,d=2

print("Enter value for a:")
a = int(input())
print("Enter value for b:")
b = int(input())
print("Enter value for c:")
c = int(input())
print("Enter value for d:")
d = int(input())

print("Before swapping")
print(f"a = {a}, b = {b}, c = {c}, d = {d}")

# Swapping the values
a, b, c, d = d, c, b, a
print("After swapping")
print(f"a = {a}, b = {b}, c = {c}, d = {d}")