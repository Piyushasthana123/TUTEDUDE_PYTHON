# w mode - open the file for writing. overwrites the file
# this is when file exist. so it overwrite the content
# fh = open("file2.txt",'wt')
# fh.write("this file is overwritten by using w mode\n")
# fh.write("this file is overwritten by using w mode")
# fh.close()

#create a new file
f = open("file3.txt",'wt')
f.write("Today is a good day")
f.close()