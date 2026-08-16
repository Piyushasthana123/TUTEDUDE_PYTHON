import copy
# using list
l1 = [3.4,2,[34,546,4],"python"]
print(id(l1)) #4317755904
print(l1) #[3.4, 2, [34, 546, 4], 'python']
#shallow copy
# l2=copy.copy(l1)
# print(id(l2)) #4319371776
# print(l2) #[3.4, 2, [34, 546, 4], 'python']

#only internal change is changing the value but direct can not be change
# l1[0]=100
# l1[2][0]=100
# print(f"l1=> {l1},{id(l1)}") #l1=> [100, 2, [100, 546, 4], 'python'],4343216640
# print(f"l2=> {l2},{id(l2)}") #l2=> [3.4, 2, [100, 546, 4], 'python'],4355039936

#deep copy
# l2=copy.deepcopy(l1)
# l1[0]=100
# l1[2][0]=100
# print(f"l1=> {l1},{id(l1)}") #l1=> [100, 2, [100, 546, 4], 'python'],4373576192
# print(f"l2=> {l2},{id(l2)}") #l2=> [3.4, 2, [34, 546, 4], 'python'],4385137344

d1 ={"id":1111,"name":"john","marks":{"eng":100,"maths":80,"chm":90.5,"bio":60.6}}
#deep copy
d2 = copy.deepcopy(d1)
d1['name']='piyush'
d1['marks']['eng']=70
print(f"d1=> {d1},{id(d1)}") #d1=> {'id': 1111, 'name': 'piyush', 'marks': {'eng': 70, 'maths': 80, 'chm': 90.5, 'bio': 60.6}},4303961920
print(f"d2=> {d2},{id(d2)}") #d2=> {'id': 1111, 'name': 'john', 'marks': {'eng': 100, 'maths': 80, 'chm': 90.5, 'bio': 60.6}},4314430912
