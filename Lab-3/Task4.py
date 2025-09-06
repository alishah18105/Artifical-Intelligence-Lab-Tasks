#You have collected information about cities in your province. You decide to store each city’s name, population, and mayor in a file. Write a python program to accept the data for a number
#of cities from the keyboard and store the data in a file in the order in which they’re entered.

f = open("cities.txt", "a")
f.write("City Name\tPopulation\tMayor\n")
choice = True
while choice:
    city_name = input("Enter the name of the city: ")
    population = input("Enter the population of the city: ")
    mayor = input("Enter the name of the mayor: ")
    
    f.write(f"{city_name}\t {population}\t, {mayor}\n")
    
    cont = input("Do you want to add another city? (yes/no): ").strip().lower()
    if cont == 'no':
        choice = False