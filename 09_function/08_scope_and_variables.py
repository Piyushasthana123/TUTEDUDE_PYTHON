# n =1 #global variable
# def func():
    # n = 5 #local variable
    # print('in',n)
# func()
# print('out',n)
#when local and global variables are present
#in 5
# out 1
#when only global variable is present
# in 1
# out 1

# n =1 #global variable
def func():
    global n # global variable is assign a local as a global variable
    n = 5 #local variable
    print('in',n)
func()
print('out',n)
#in 5
# out 5