#.py file is a module
#built-in module
#math , ramdom , datetime,....

#how to import a module in python
#syntax:import module_name
#syntax:for importing only few functions/variables: from module_name import func1,func2,func3
#syntax:  to create an alias  for the module that is imported: import module_name as alias_name

import math
#calculating square root of number
num = 100
output = math.sqrt(num)# module function_name(arg1,arg2,....)
print(f"square root of {num} is : {output}")
#square root of 100 is : 10.0


#calculating the area of circle
radius = 5
area_of_circle = math.pi*(radius**2)
print(f"area of circle with radius {radius} is : {area_of_circle}")
#area of circle with radius 5 is : 78.53981633974483


#throw a die
from random import randint
value = randint(1,6)
print(value)

#datetime module with alias
import datetime as dt
# t = dt.datetime.now() #2026-09-03 22:10:32.340953
t = dt.time(8,43,51) #08:43:51
print(t)
