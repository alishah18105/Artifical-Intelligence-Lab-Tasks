# Try the scenrio below: 
# Make a program that lists the countries in the set 
# clist = ['Canada','USA','Mexico','Australia'] 

clist = []
print("Enter the names of countries (type 'done' to finish):")
while True:
    country = input("Enter country name: ")
    if country.lower() == 'done':
        break
    clist.append(country)

for country in clist:
    print(country)