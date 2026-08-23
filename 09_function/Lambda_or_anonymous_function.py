
def add_1(num,num1):
    return num + num1
print(add_1(3,5)) #8

#by using lambda function

# syntax
# lambda argument : expression
func=lambda num,num1 : num+num1
res = func(3,5)
# print(res) #6
print(res) #8