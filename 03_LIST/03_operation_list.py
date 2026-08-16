"""
extend()
pop()
remove()
"""

# extend()
fruits = ["apple", "banana", "cherry","apple"]
# print(fruits)
# fruits.extend(["banana","mango"]) #['apple', 'banana', 'cherry', 'banana', 'mango']
#fruits.append(["banana","mango"]) #['apple', 'banana', 'cherry', ['banana', 'mango']]
print(fruits)
# print(len(fruits))

# remove()
# fruits.remove("banana")
fruits.remove("apple")
# print(fruits) #['apple', 'cherry']
print(fruits) #['banana', 'cherry', 'apple']

fruits.pop()
print(fruits) #['apple', 'banana']