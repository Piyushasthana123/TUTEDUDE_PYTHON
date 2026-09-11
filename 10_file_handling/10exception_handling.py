# FileNotFoundError: [Errno 2] No such file or directory: 'practice3.txt'

try:
    f= open("file12.txt",'rt')
    data=f.read()
    f.close()
except FileNotFoundError as file_error:
    print("the  file is not found!!")
    print(file_error)
else:
    print(data)
finally:
    print("finally block")
# if there is an error the then it goes to except then it directly goes to finally block
# the file is not found!!
# [Errno 2] No such file or directory: 'file12.txt'
# finally block