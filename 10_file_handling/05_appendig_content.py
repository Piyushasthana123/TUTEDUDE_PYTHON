# 'a' mode => is use to append the content
# if file do not exist , 'a' mode creat the file.
# f = open("file2.txt",'at')
f = open("file4.txt",'at')
f.write("\nthis is the new text of the file which is appended.")
f.write("\nthis is the new text of the file which is appended.")
f.write("\ngood day all!")
f.close()