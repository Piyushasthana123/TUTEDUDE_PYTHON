# JSON - JavaScript object notation

import json
students= {
    'student1':{'roll':101 ,'name':'john', 'percent' : 92.5,'sports': False},
    'student2':{'roll':102 ,'name':'carol', 'percent' : 93.5,'sports': True },
    'student3':{'roll':103 ,'name':'alice', 'percent' : 87.5,'sports': False}
}

#
# print(student)
# print(type(student))

# dump()
# with open('students.json', 'w') as file:
#     json.dump(students, file,indent = 4)

#load()
# with open('students.json', 'r') as file:
#     data=json.load(file)
# print(data)
# print(type(data))

try:
    # update()
    # read the old data from the json file
    with open('students.json', 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    with open('students.json', 'w') as file:
        json.dump(students, file, indent=4)
else:
    # update operation
    data.update(students)
    # dump()-write the json data in the json file
    with open('students.json', 'w') as file:
        json.dump(data, file,indent = 4)

# update()
# read the old data from the json file
# with open('students.json', 'r') as file:
#     data = json.load(file)
#update operation
# data.update(students)

#dump()-write the json data in the json file
# with open('students.json', 'w') as file:
#     json.dump(data, file,indent = 4)