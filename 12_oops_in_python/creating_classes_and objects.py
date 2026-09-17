# creating the class

class MyClass: # both the world will stat with capital letters
    pass

#creating the objects
obj1 = MyClass()
obj2 = MyClass()

#obj1 and obj2 are objects of class MyClass

l1 = [10,20,30]
print(type(l1))
print(type(obj1))
print(type(obj2))
"""
<class 'list'>
<class '__main__.MyClass'>
<class '__main__.MyClass'>
"""
#calling methods using objects
# obj1.methods(arg1,arg2,...)


class Students:
    """
    this is a class student to manage student information and activities
    """
    pass
s1 = Students()
s2 = Students()

#doc string => it is documents or the details about the class, when we create the class we can provide documentation
# you can use __doc__
print(Students.__doc__) #this is a class student to manage student information and activities
help(Students)
