# __init__() method
# is a instance method
# is used to create and initialize the attribute during the object creation

class Students:
    """
    This is a class Students to manage students info and activities
    """
    def __init__(self,name,roll_no,dept):
        print(f'calling the Initializer!! {self}')
        self.name = name
        self.roll_no = roll_no
        self.department = dept

    # default positional arguments  1 was already given
    def study(self,n_hours):
        print(f"self is : {self}")
        print(f"the student studies for {n_hours} hours a day")
    def sport(self, sport_name):
        print(f"the student plays {sport_name} sport")


student1=Students("piyush",123,"CSE")
#object_name.attribute_name= value
# student1.name = "piyush"

student2 = Students("priya",456,"AI/ML")
# student2.name="fuker"

print(student1.name , student1.roll_no, student1.department)
print(student2.name , student2.roll_no, student2.department)
"""
instance variable/ attributes are different for different objects    
"""
print(student1.__dict__)
print(student2.__dict__)
"""
calling the Initializer!! <__main__.Students object at 0x10295aa50>
calling the Initializer!! <__main__.Students object at 0x10337ca50>
piyush 123 CSE
priya 456 AI/ML
{'name': 'piyush', 'roll_no': 123, 'department': 'CSE'}
{'name': 'priya', 'roll_no': 456, 'department': 'AI/ML'}
"""
print("---------------------------------------------- ---------")
student1.grade ="B"
print(student1.__dict__)
print(student2.__dict__)