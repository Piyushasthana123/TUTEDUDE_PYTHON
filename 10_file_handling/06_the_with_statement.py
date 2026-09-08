# this the opening file manually and close file manually
# f= open("file4.txt","rt")
# contents = f.read()
# f.close()
# print(contents)

#
# with open("file4.txt",'rt')as f:
#     print(f.read())

with open("practice_2.txt",'xt')as f:
    f.write("new file has been created")
    f.write("\ngood buy!")
