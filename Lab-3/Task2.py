#a Python program to find if a given string starts with a given character using Lambda
string = "Python"
character = "P"

starts_with = lambda x,y: string.startswith(character)
result = starts_with(string,character)
print(f"Does the string '{string}' start with '{character}'?: {result}")