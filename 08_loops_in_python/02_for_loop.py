# # string
# s1 ="Hello world"
# for char in s1:
#     print(char)
# print("End of loop")

# dic
employee ={"empid":1001 , "name":"john","Department":"HR"}
# for i in employee:
#     print(i) # it only print the key
#empid
# name
# Department


# for i in employee:
#     print(i,":",employee[i]) #it print both key and values
# empid : 1001
# name : john
# Department : HR

print(employee.items())

for i in employee.items():
    # print(i) # it give key nad value pairs in tuples
# dict_items([('empid', 1001), ('name', 'john'), ('Department', 'HR')])
# ('empid', 1001)
# ('name', 'john')
# ('Department', 'HR')

    print(i[0], ":", i[1])  # key and value
# empid: 1001
# name: john
# Department: HR
