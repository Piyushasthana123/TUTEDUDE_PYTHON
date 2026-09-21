""""
class methods are methods defined inside the class that are bound to the class
to create a class method, we use decorators => classmethod
"""
# class Welcome:
#
#      @classmethod
#      def greed(cls):
#          print(cls)
#          print("Welcome to the Class Method")
# w1=Welcome()
# w1.greed()
# print(Welcome)

# <class '__main__.Welcome'>
# Welcome to the Class Method
# <class '__main__.Welcome'>


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

    @classmethod
    def greed(cls):
        print(cls)
        print(f"Welcome to {cls.college_name}")


    @classmethod
    def get_department(cls):
        print(f"Department of {cls.college_name} are:")
        for dept in cls.departments:
            print(dept)

student1 = Students("John",1234)
student1.study(100)
student1.greed()
student1.get_department()
