"""
reverse()
count()
sort()
membership operation
"""

days_of_week = ["mon","tue","wed","thur","fri","sat","sun"]
print(days_of_week)
#reverse
# days_of_week.reverse()
# print(days_of_week) # ['sun', 'sat', 'fri', 'thur', 'wed', 'tue', 'mon']

#sort
num = [1,4,78,45,33,90,22,10]
num.sort(reverse=True)
print("sorted list: ",num) #sorted list:  [90, 78, 45, 33, 22, 10, 4, 1]
print("descending sorted list: ",num) #descending sorted list:  [90, 78, 45, 33, 22, 10, 4, 1]

#count()
numbers = [0,4,3,3,2,2,1,1,9,9,9,5,5,5,5,6,7,7,8]
print(numbers.count(5)) # 4

#in and not in membership operator
lang = ["python","java","c","c++","go","ruby","javascript"]
print("python" in lang)  #True
print("react" in lang) #False
print("react" not in lang) #True