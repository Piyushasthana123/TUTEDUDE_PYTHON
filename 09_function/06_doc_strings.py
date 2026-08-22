# doc_string

# def func():
#     """
#     this is a docstring
#     we can write what the function does here
#     :return:None
#     """
#
#     return None
# func()
# print(help(func))


# Help on function func in module __main__:
#
# func()
#     this is a docstring
#     we can write what the function does here
#     :return:None
#
# None

def divide(num1,num2):
    """
    num1: A Number to be divided(Numerator)
    num2: A Number to be divides(Denominator)
    :return:float{if num2 is non zero) or str(if num2 is zero)
    """
    if num2 == 0:
        return "can't divide by zero"
    else:
        return num1/num2
print(divide(10,4))
# print(help(divide))

#Help on function divide in module __main__:
# divide(num1, num2)
#     num1: A Number to be divided(Numerator)
#     num2: A Number to be divides(Denominator)
#     :return:float
#
# None
