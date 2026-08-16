student1 ={"maths":80.5, "eng":76.5,"phy":89.0}
# print(student1)

#fetch the marks of phy
# print(student1["phy"])
# print(student1["chm"]) #KeyError: 'chm'

#get()
# print(student1.get("phy"))
# print(student1.get("chm")) # None
# print(student1.get("chm",40.0)) #40.0

emp1 ={"id": 1001,"name":"piyush","salary":500000}
# print(emp1.get("phone",9876543210)) #9876543210
# print(emp1.get("id",9876543210)) #1001

#MEMBERSHIP OPERATOR => IN OR NOT IN only use for key not for values
# print(1001 in emp1) #False
# print('name'in emp1) #True

#add new key:value pairs
emp1['phone']=987654321
# print(emp1) #{'id': 1001, 'name': 'piyush', 'salary': 500000, 'phone': 987654321}

sem1_mark = {"math":80.0,"eng":76.5,"phy":89.0}
sem2_mark = {"chm":81.5,"bio":90.5}
# update()
sem1_mark.update(sem2_mark)
print(sem1_mark) #{'math': 80.0, 'eng': 76.5, 'phy': 89.0, 'chm': 81.5, 'bio': 90.5}

#pop()
#use to delete the key value pairs by using key
sem1_mark.pop('math')
# print(sem1_mark) #{'eng': 76.5, 'phy': 89.0, 'chm': 81.5, 'bio': 90.5}

#key cannot be duplicated in dictionaries
groceries_1={"milk":60,"rice":100,"bread":200,"milk":65}
print(groceries_1) # {'milk': 65, 'rice': 100, 'bread': 200}
