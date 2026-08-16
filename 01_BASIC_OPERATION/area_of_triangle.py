""""
when all the length of the sides of triangle is known- a,b,c
semi perimeter(s)= (a+b+c)/2
area = square root of (s * (s-a) * (s-b) * (s-c))
"""

a=float(input("Enter the first side value: "))
b=float(input("Enter the second  side value: "))
c=float(input("Enter the third side value: "))
s= (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**(1/2)
print("The area of the triangle is ",round(area,2))