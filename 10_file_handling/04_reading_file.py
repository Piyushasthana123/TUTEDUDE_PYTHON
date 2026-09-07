# reading the file
# f.read() - this function read the content of the file
# open the  file in 'rt' read text mode so file as string

f = open("preactice.txt",'rt')
#readlines() - it fetches all the line together
print(f.readlines())
print(type(f.readlines())) #<class 'list'> or ["this file is created using the 'x' mode in python\n", "this file is created using the 'x' mode in python"]


#readline()
print(f"line1: {f.readline()}") # this read the only one line with \n
print(f"line2: {f.readline()}")
print(f"line3: {f.readline()}")
print(f"line4: {f.readline()}") #empty string => the file has reached End of file error(EOF)

# line1: this is the text file
#
# line2: we are learning file handling in python.
#
# line3: mode to open file are : r,x,w,a,t,b




# print(f.read(1)) # it only read the first characters 't'
# print(type(f.read()))
f.close()
#this is the output
# this is the text file
# we are learning file handling in python.
# mode to open file are : r,x,w,a,t,b
#<class 'str'>
