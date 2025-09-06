
numbers = [2,3,4,5,6,7,8,9,10]
squares = lambda x: x**2
cubes = lambda x: x**3
print("Number\tSquare\Cube\n")
for i in numbers:
    print(f"{i}\t{squares(i)}\t{cubes(i)}")
    