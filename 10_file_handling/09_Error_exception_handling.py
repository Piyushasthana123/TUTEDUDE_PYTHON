"""
complete time error => syntax error or  indentation error
Exceptions => errors during execution
 """
#
# age = 24
# # print(age #SyntaxError: '(' was never closed
# if age >= 18:
# # print(age) #IndentationError: expected an indented block after 'if' statement on line 7
#     print(age)
# man = age+y #NameError: name 'y' is not defined
# print(man)

# how to handle exception? =>try-except block

# we have ZeroDivisionError: division by zero

try:
    num = int(input("Enter a number: "))
    num2 = int(input("Enter a another number: "))
    result = num / num2
    print(result)
except ZeroDivisionError:
    print("the Denominator can not be zero")
except ValueError:
    print("The value entered is not a number") #Enter a number: d
                                               # The value entered is not a number
# Enter a number: 10
# Enter a another number: 0
# the Denominator can not be zero