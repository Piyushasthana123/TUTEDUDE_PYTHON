# instance method -
# method define inside a class which is bound to /associated with the instance/object

# help(list)

class Students:
    """
    This is a class Students to manage students info and activities
    """
    # default positional arguments  1 was already given
    def study(self,n_hours):
        print(f"self is : {self}")
        print(f"the student studies for {n_hours} hours a day")
    def sport(self, sport_name):
        print(f"the student plays {sport_name} sport")


student1=Students()
# print(f"object is:  {student1}")
student1.study(100)
student1.sport("Football")

print("----------------------------------------------------------")

student2=Students()
# print(f"object is:  {student2}")
student2.study(666)
student2.sport("soccer")

"""
when we call an instance method using the object/instance of the class , python passes the object itself
as the first argument to that method
that first argument is by standard is self
"""