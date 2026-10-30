# a = 10
# b = 15
# print(a+b) # a.__add__(b) => int.add(a,b)
#
# class A:
#     def f1(self, n):
#         pass
# obj = A()
# obj.f1(20) # A.f1(obj,20)
#
# s1 = "hello"
# s2 = "world"
# print(s1+s2) #str.__add__(s1 ,s2)
#
# help(int)

class rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def __add__(self, other):
        return self.height
r1 = rectangle(10, 20)
r2 = rectangle(12, 30)

print(r1.area())
print(r2.area())
print(r1 + r2)

print(r1 + r2)