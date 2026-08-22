#*args(arges ki jagha kuch bhi rehe sakta hai) argument-
# it allwoded the variable length positional arguments of (0 to n)
# def add(*args):
    # print(args,type(args)) #(10, 20, 34, 30, 45, 1, 2, 3, 4) <class 'tuple'>
    # return sum(args)
# add(10,20)
# result=add(10,20,34,30,45,1,2,3,4)
# print(f"result is {result}")  #result is 149
# result=add() # empty the all parameters of a function
# print(f"result is {result}") #result is 0

# def student_details(sid,sname,*marks):
#     if len(marks) == 0:
#         print(f"{sname} with id {sid} was absent in all exams!")
        #rahul with id 103 was absent in all exams!
    # else:
    #      percent = sum(marks)/len(marks)
    #      print(f"{sname} with {sid} secured {percent}%")
# student_details(101,"Jean",89,70,68,85,65,70) #Jean with 101 secured 74.5%
# student_details(102,"carol",92.4,90,80.5,90,89,85.5) #carol with 102 secured 87.89999999999999%
# student_details(103,"rahul")

# **kwargs - variable length keyword arguments
#the arguments cannot follow var -keyword argument

# def func(**kwargs):
    # print(kwargs,type(kwargs))
# func(x=10,y=20,z=30) # #{'x': 10, 'y': 20, 'z': 30} <class 'dict'>
# func() # {} <class 'dict'>


def student_details(sid, sname,*extra, **marks):
    if len(marks) == 0:
        print(f"{sname} did not attend any Exams")
    else:
        percent = sum(marks.values( )) / len(marks)
        print(f"{sname} with id {sid} secured {percent}%")
    print(f"{sname} does {extra} ") #John does ('football',) 
student_details(101,"John","football", sub1 = 70, sub2 = 80,sub3 = 90,sub4 = 50)
# John with id 101 secured 72.5%