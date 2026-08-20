# def even_odd(num):
#      if num % 2 == 0:
#          # print("even number")
#          return "even number" #even number
#      else:
#          return "odd number" #odd number
#          # print("odd number")
#          #odd number
#          # None
# result = even_odd(7)
# print(result)
# result2 = even_odd(20)
# print(result2)


# def add(a,b):
#     return a+b
# VAL_1= int(input("Enter a number: "))
# VAL_2= int(input("Enter another number: "))
# add1 = add(VAL_1,VAL_2)
#add1 = add(10,20)
# add2 = add(-10,20)
# print(add1) #30 ,-60
# print(add2) #10

def arithmetics(num1, num2):
    res1=num1 + num2
    res2=num1 * num2
    res3=num1 / num2
    return res1,res2,res3
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
rs1,rs2,rs3 = arithmetics(num1,num2)
print(f"sum of two number is {rs1}")
print(f"multiply of two number is {rs2}")
print(f"division of two number is {rs3}")
""" 
Enter first number: 20
Enter second number: 5
sum of two number is 25
multiply of two number is 100
division of two number is 4.0
"""