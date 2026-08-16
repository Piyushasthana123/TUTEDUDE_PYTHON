# Tuple
# (item,item,item...)
# sequence of item as a collection
t1=("python",2,4.5,[1,2,3],(9,7,10),True,None)
# print(t1)
# print(len(t1))

#Accessing item of a tuple - index
# print(t1[0])
# print(t1[-1])

#crate a tuple
t2= 10,20,30,40
#print(t2) #(10, 20, 30, 40)
# print(type(t2))

# type casting
l1 = [1,2,3,4,5]
# print(l1,type(l1)) # [1, 2, 3, 4, 5] <class 'list'>
 # t3=tuple(l1)
# print(t3,type(t3)) # (1, 2, 3, 4, 5) <class 'tuple'>

fruits =("mango","banana","apple")
print(fruits,type(fruits))
l_fruits =list(fruits) # ('mango', 'banana', 'apple') <class 'tuple'>
print(l_fruits,type(l_fruits)) #['mango', 'banana', 'apple'] <class 'list'>