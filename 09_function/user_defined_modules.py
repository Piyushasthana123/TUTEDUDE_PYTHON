"""
simple arithmetics module: arithmetics.py
"""
def add(num1,num2):
    return num1+num2
def square_root(num):
    return num ** 0.5

#it use directly
# a = 10
# b = 20
# result = add(a,b)
# print(result) #30

# when you run  the code when it imported this program can not de executed
if __name__ == "__main__":
    a = 10
    b = 20
    result = add(a,b)
    print(result)
# for 13_imported_code.py => __name__ => "__main__"
# for  user_defined_modules.py => __name__ => "arithmetic"