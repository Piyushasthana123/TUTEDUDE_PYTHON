"""
class variable is defined at class level
same copy of the class variables are shared among the objects
"""

class Students:
    """
    This is a class Students to manage students info and activities
    """
    college_name="ABC college"
    departments = ["Arts","Commerce","Science"]
    def __init__(self, name, roll_no):
     print(f'calling the Initializer!! {self}')
     self.name = name
     self.roll_no = roll_no


    # default positional arguments  1 was already given


    def study(self, n_hours):
        print(f"self is : {self}")
        print(f"the student studies for {n_hours} hours a day")


    def sport(self, sport_name):
        print(f"the student plays {sport_name} sport")

student1 = Students("john",1234)
# help(Students)
# print(student1.__dict__)
print(student1.college_name)
print(student1.departments)
