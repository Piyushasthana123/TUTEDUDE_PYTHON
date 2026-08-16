# s1 = {1,2,3,4,5,6,7,8,9}
# s1.add(-1)
# print(s1)#{1, 2, 3, 4, 5, 6, 7, 8, 9, -1}

#frozen 05_sets - immutable 05_sets
fs1 = frozenset({10,20,30,4})
print(fs1,type(fs1)) #frozenset({10, 20, 4, 30}) <class 'frozenset'>
# fs1.add(40)
# print(fs1) #AttributeError: 'frozenset' object has no attribute 'add'

fs2 = frozenset({10,50,60,100,200})
print(fs2,type(fs2))#frozenset({50, 100, 200, 10, 60}) <class 'frozenset'>

print(fs1 & fs2) #frozenset({10})

print(fs1 | fs2) #frozenset({4, 100, 200, 10, 50, 20, 60, 30})

print(fs1 - fs2) #frozenset({20, 4, 30})
print(fs2 - fs1) #frozenset({200, 50, 100, 60})

