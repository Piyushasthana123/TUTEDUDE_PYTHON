#set are non-sequential collection of items
# comma separated elements enclosed within {}
from calendar import weekday

# set1 ={10,"python",2.4}
# print(set1) #{10, 2.4, 'python'}
# print(type(set1)) #<class 'set'>

#cannot have indexing with 05_sets
# print(set1[0]) #TypeError: 'set' object is not subscriptable

#length of the set
# print(len(set1)) #3

#05_sets do not allow duplicate elements
# l1= [10,2.4,10,30,20]
# print(l1,type(l1)) #[10, 2.4, 10, 30, 20] <class 'list'>
# l2= {10,2.4,10,30,20}
# print(l2,type(l2)) #{10, 2.4, 20, 30} <class 'set'>

nums1 = {1,3,2,0,-1}
nums2 = {3,5}
#membership operator - in or not in
# print(0 in nums1) #True
# print(10 in nums1) #False

#concatenation ?
# print(nums1 + nums2) #TypeError: unsupported operand type(s) for +: 'set' and 'set'

#repeating 05_sets?
# print(nums1*2) #TypeError: unsupported operand type(s) for *: 'set' and 'int'

weekdays=("mon","tue","wed","thur","fri","sat","sun")
# weekdays = set(weekdays)
# print(weekdays) #{'fri', 'tue', 'thur', 'sun', 'wed', 'mon', 'sat'}

#are 05_sets mutable or immutable?
set1={2,0,4,-1}
print(set1) #{2,0,4,-1}

#add()
# set1.add(5)
# print(set1) #{0, 2, 4, 5, -1}

#remove()
set1.remove(0)
print(set1) #{2, 4, -1}

#discard()
set1.discard(-1)
set1.discard(10) #no error simply print
print(set1) #{2, 4}

