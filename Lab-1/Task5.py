# Write a list comprehension which, from a list, generates a lowercased version of each string that has
# length greater than five. 

words = ["HELLO", "PYTHON", "WORLD", "PROGRAMMING", "CHATGPT"]
newList = [words[i].lower() for i in range(len(words)) if len(words[i])>5]

print("Lowercased words with length greater than five:", newList)
