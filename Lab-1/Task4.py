# Write a Python program to count the number of strings where the string length is 2 or more and the
# first and last character are same from a given list of strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2. 

list = ['abc', 'xyz', 'aba', '1221']
count  = 0
for string in list:
    if len(string) >= 2 and string[0] == string[-1]:
        count += 1
print("Number of strings with same first and last character:", count)