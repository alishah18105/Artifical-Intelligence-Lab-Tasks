# Create a loop that counts all even numbers to 10 
sum_even = 0
for i in range(1,11):
    if i % 2 == 0:
        sum_even += i
print("The sum of even numbers from 1 to 10 is:", sum_even)
