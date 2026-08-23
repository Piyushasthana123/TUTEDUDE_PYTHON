# In python , we can pass a function as argument of another function
def add_1( num):
    return num+1
# print(add_1(10))

def square(num):
    return num**2
# print(square(10))
num = int(input("Enter a number: ")) #99
# res_1 = add_1(num)
# res_2 = square(res_1)
# print(res_1) #100
# print(res_2) #10000

result = square(add_1(num))
print(f"The result of {num} is {result}")
# Enter a number: 3
# The result of 3 is 16 