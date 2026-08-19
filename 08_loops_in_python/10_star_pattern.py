#right angle triangle
for i in range(1,6): #how many row to print
    for j in range(1,i+1): # how many stars to print
        print("*", end=' ') # give the end with empty space
    print() #this redirect to next line
# *
# * *
# * * *
# * * * *
# * * * * *

for i in range(1,6): #how many row to print
    for j in range(1,i+1): # how many stars to print
        print(i, end=' ') # give the end with empty space
    print()
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5