# is not allowed - list,set,dic - mutable data type
#is allowed - int,float,bool,str,tuple - immutable data type
#keys of dictionaries can only be immutable data type


#keys cannot be list
# d1 ={[1,2,3] : 9,[4,5,6] : 7,[7,8,9] : 10}
# print(d1) #TypeError: unhashable type: 'list'

#keys cannot be use as a set
# d ={{1,2,3} : 9,{4,5,6} : 7}
# print(d)TypeError: unhashable type: 'set'

#dic is cannot be use as key value pair in dic
# d0={{'a':2,'b':2}:8}
# print(d0) #TypeError: unhashable type: 'dict'

#(allowed key as a str,int,float,bool,tuple
#               and
# values can have any datatype)

#str
# d2={"Nine" : 9,"Ten":10}
# print(d2) #{'Nine': 9, 'Ten': 10}

#int
d3 ={1:True,0:False}
# print(d3) #{1: True, 0: False}

# bool
d5 = {True:1,False:0}
# print(d5) #{True: 1, False: 0}

#tuple
d4 ={(1,2,3) : 9,(4,5,6) : 7,(7,8,9) : 10}
# print(d4) #{(1, 2, 3): 9, (4, 5, 6): 7, (7, 8, 9): 10}

#value can be any datatype
student_1={"id":1001,"name":"john","marks":[80.0,50.6,90.7]}
student_2={"id":1001,"name":"john","marks":{'eng':80.0,'maths':50.6,'chm':90.7}}
# print(student_1)#{'id': 1001, 'name': 'john', 'marks': [80.0, 50.6, 90.7]}
# print(student_1['marks'][0]) #80.0
# print(student_2['marks']['maths']) #50.6

#fetch the only keys
#by using key()
# print(student_1.keys(),type(student_1.keys())) #dict_keys(['id', 'name', 'marks']) <class 'dict_keys'>
# by using values()
# print(student_1.values(),type(student_1.values())) #dict_values([1001, 'john', [80.0, 50.6, 90.7]]) <class 'dict_keys'>

#items() it fetch the key value pairs
print(student_2.items(),type(student_2.items()))
#dict_items([('id', 1001), ('name', 'john'), ('marks', {'eng': 80.0, 'maths': 50.6,
# 'chm': 90.7})]) <class 'dict_items'>