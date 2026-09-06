#creating the file in text  - xt or tx
f = open('file1.text','xt')

#write into the file
#write(content)
f.write("this file is created using the 'x' mode in python \n")
f.write("this file is created using the 'x' mode in python ")

f.close()