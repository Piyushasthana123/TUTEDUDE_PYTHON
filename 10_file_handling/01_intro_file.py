# opening the file in python
#open(file_name , mode_to_open)
# #mode - r,x, a, w,t,b,=> 'rt' are the default mode

f = open("preactice.txt",'rt')
print(f)#<_io.TextIOWrapper name='preactice.txt' mode='rt' encoding='UTF-8'>
# read operation
print(f.read())
# close the file
f.close()