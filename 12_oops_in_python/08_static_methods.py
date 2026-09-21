"""
static method is defined inside the class which is neither bound to the object nor to the class
to create a static method , we use staticmethod decorator
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
        print(self)
        print(f"the student studies for {n_hours} hours a day")


    def sport(self, sport_name):
        print(f"the student plays {sport_name} sport")

    @staticmethod
    def greed():
        print(f"Welcome to the college")


    @classmethod
    def get_department(cls):
        print(f"Department of {cls.college_name} are:")
        for dept in cls.departments:
            print(dept)

# help(Students)

student1=Students("John",1234)
student1.study(5)
student1.get_department()
student1.greed()