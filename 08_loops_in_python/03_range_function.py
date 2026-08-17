#range - built in function used to generate sequence of integers in the give interval
#range(start,stop,sep) stop is not included

# for i in range(start,stop,step):
#         statements

# for i in range(1,11,1):
#     print(i) #1,2,3,4,5,6..,9.10


# for i in range(1,11,2):
#     print(i) #1,3,5,7,9
#

# generate even number btw 1 to 10 (10 is excluded)
# for i in range(2,10,2):
#     print("generate even number btw 1 to 10",i)
# generate even number btw 1 to 10 2
# generate even number btw 1 to 10 4
# generate even number btw 1 to 10 6
# generate even number btw 1 to 10 8

# reverse order => 20 to 10 (10 is excluded)
# for i in range(20,10,-2):
#     print(i) #20, 18, 16, 14, 12

#countdown from 10 to 1 for happy new year
# for i in range(10,0,-1):
#     print(i)
# print("happy new year" )
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# happy new year

#range(start,stop)=> step = 1 by default
# for i in range(1,5): #step = 1
#     print(i) #1,2,3,4

# range(stop)=> 0 to stop-1 with  a step of 1, start = 0 by default
# for i in range(5): #start = 0 ,step = 1
#     print(i) #0,1,2,3,4

groceries =["milk","sugar","salt"]
# for grocery in groceries:
#     print(grocery)
# milk
# sugar
# salt
# for grocery in range(len(groceries)):
#     print(grocery) #0,1,2 these are the index of the groceries

profit =[10,11,9,6]
for i in range(len(profit)):
    q = i +1
    print(f"profit for quater {q} is {profit[i]}")
# profit for quater 1 is 10
# profit for quater 2 is 11
# profit for quater 3 is 9
# profit for quater 4 is 6
