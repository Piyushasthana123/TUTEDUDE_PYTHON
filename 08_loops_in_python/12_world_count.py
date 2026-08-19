Countries_Name =["India","united state","australia","Ireland","Sri Lanka","Iceland","Cuba","Iran","Poland"]
# Count all the countries which are start with "I"
count = 0
list_countries = []
for country in Countries_Name:
    # if country[0] == "I":
    if country.startswith("I"): #  use it with string
        count = count + 1
        list_countries.append(country)

print(list_countries) 
print(f"total number of countries start with 'i' is {count}")


