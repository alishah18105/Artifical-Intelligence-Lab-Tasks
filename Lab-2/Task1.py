# Cabinets and Boxes are objects that are mostly in cubic shape. Make a program that takes 
# inputs like height, width and depth from user and then calculate volume of the cube: 
# volume = height ∗ width ∗ depth 
# After calculating volume of cube, compare it with following ranges and print the relevant label: 

height = float(input("Enter the height of the cube: "))
width = float(input("Enter the width of the cube: "))   
depth = float(input("Enter the depth of the cube: "))

volume = height * width * depth

if(volume <= 10):
    print("The volume of the cube is Extra Small.")
elif(volume <= 25):
    print("The volume of the cube is Small.")
elif(volume <= 75):
    print("The volume of the cube is Medium.")
elif(volume <= 100):
    print("The volume of the cube is Large.")
elif(volume <= 250):
    print("The volume of the cube is Extra Large.")
else:   
    print("The volume of the cube is Extra Extra Large.")