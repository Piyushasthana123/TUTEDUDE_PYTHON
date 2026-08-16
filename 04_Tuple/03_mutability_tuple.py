# mutability & Immutability
# list are mutable
#tuple and string are immutable

s1= "python is fun"
# s2 = s1.replace("python","java")
# print(s1) # python is fun
# print(s2) # java is fun

t1 = ("mango","apple","orange")
# t1.append("banana")
# print(t1) #AttributeError: 'tuple' object has no attribute 'append'

# l1 = ["mango","apple","orange"]
# print(id(l1)) #4337535424 memory address
# l1.append("banana")
# print(l1) #['mango', 'apple', 'orange', 'banana']
# print(id(l1))#4337535424 memory address

l1 = ["mango","aple","orange"]
l1[-2]="apple"
print(l1) #['mango', 'apple', 'orange']
print(id(l1)) #4369250816 memory address

s2 = "python is fun"
print(s2)
s2[0]="p"
print(s2) #TypeError: 'str' object does not support item assignment
