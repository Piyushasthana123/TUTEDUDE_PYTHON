# type of inheritance
#single level inheritance
#multi level inheritance
#multiple level inheritance

# single level inheritance
class A:
    def start_1(self):
        print("A1")
    def start_2(self):
        print("A2")
class B:
    def start_3(self):
        print("B3")
    def start_4(self):
        print("B4")


# Multi _ level _ inheritance
class C(A,B):
    def start_5(self):
        print("C")
    def start_6(self):
        print("C6")
#single level
# a = A()
# b = B()
# c = C()
# a.start_1()
# b.start_3()
# c.start_6()

#multi level
a = A()
a.start_2()

b = B()
b.start_3()

c = C()

c.start_1()