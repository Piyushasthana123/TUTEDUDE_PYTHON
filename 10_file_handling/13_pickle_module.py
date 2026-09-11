import pickle
students= {
    'student1 ':{'roll':101 ,'name':'john', 'percent' : 92.5,'sports': False},
    'student2':{'roll':102 ,'name':'carol', 'percent' : 93.5,'sports': True },
    'student3':{'roll':103 ,'name':'alice', 'percent' : 87.5,'sports': False}
}
print(students)
print(type(students))

"""
with open("student_info.txt",'xt') as f:
f.write(str(students))

with open("student_info.txt",'rt') as f:
    content = f.read()
print(type(content)) #<class 'str'>
"""

#serialization : how to store the data
# with open("student_info2.bin",'bx') as f:
#     for student in students :
#         pickle.dump(students[student],f)

#deserialization : how to get that data back in it data type
#print the name of student who score 90 or more marks
with open("student_info2.bin",'rb') as f:
    # data1 = pickle.load(f)
    # print(data1,type(data1))
    # data2 = pickle.load(f)
    # print(data2,type(data2))
    # data3 = pickle.load(f)
    # print(data3,type(data3))
    # data4 = pickle.load(f)
    # print(data4,type(data4))
    students_list = []
    while True:
        try:
            data = pickle.load(f)
            # print(data, type(data))
            if data['percent'] >=90:
                print(data['name'])
                students_list.append(data['name'])
        except EOFError:
            print("file is loaded successfully")
            break
print(students_list)
