def add(a,b):
    return a+b

#positional arguments - passing the arguments in order of their position
result = add(14,2)
print(f"result is {result}") #result is 16

#Default arguments
# def add(a,b=10):
#     print(f"a = {a} , b = {b}") #a = 10 , b = 10
#     return a+b
# result = add(10)
# print(f"result is {result}") #result is 20

# def add(a,b=10,c):# positional argument not come after the default arguments
#     print(f"a = {a} , b = {b} , c = {c}") #a = 10 , b = 10
#     return a+b+c
# result = add(10,20,40)
# print(f"result is {result}") #SyntaxError: parameter without a default follows parameter with a default

def add(a,b=20 , c=10):
    print(f"a = {a} ,c = {b} ,c ={c}")
    return a+b+c
# keyword arguments
result = add(14,c=2, b=10) #a = 14 ,c = 10 ,c =2
print(f"result is {result}") #result is 26

