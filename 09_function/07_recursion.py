"""
recursion is a process in which a function call itself till a certain condition is not met.
factorial of n - n*(n-1)*(n-2)*(n-3).....2*1
n!
4! = 4*3*2*1=24

there are 2 parts of recursive condition
1. base/terminal condition
2. recursive condition
n! = n * (n-1)*(n-2)*(n-3).....
n! = n * (n-1)!
n! = n * (n-1) * (n-2)!
"""
#this is without recursion
# def factorial(n):
#     factorial = 1
#     while n>1:
#         factorial *= n
#         n -= 1
#     return factorial
# num= int(input("Enter a number: "))
# print(factorial(num))

#with recursion
def factorial_recursive(num):
        if num == 1 or num == 0:
            return 1
        else:
            factorial = num*factorial_recursive(num-1)
            return factorial
num =int(input("Enter a number: "))
print(f"factorial of {num} is : {factorial_recursive(num)}")
#Enter a number: 5
# factorial of 5 is : 120


