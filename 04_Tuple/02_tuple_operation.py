"""
concatenation , repetition, membership,
count,index,min,max,sum
"""
student_detail1= (1001,"john")
student_detail2= (78.5,91.0,83.7,79.6)

# +( concatenation )
#student_datails=student_detail1+student_detail2
#print(student_datails) #(1001, 'john', 78.5, 91.0, 83.7, 79.6)

# * (repetition)
# t1 = ("class 5",50000)
# print(t1*3)

# in or not in ( membership)
print(91.0 not in student_detail1) #True
print(91.0 not in student_detail2) #False
print(91.0  in student_detail2) #True

#count()
t1 = (10,4,9,1,0,3,1)
#tuple.count(element)
print(t1.count(1)) #2

# index()
#tuple.index(element)
print(t1.index(4)) #what is the index of 4 in tuple t1? #1


