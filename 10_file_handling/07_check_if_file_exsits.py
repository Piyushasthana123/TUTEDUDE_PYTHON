#os.path.exists()
import os
# file_name = "preactice.txt"
# file_name = "preactic.txt "
# file_name = "/Users/piyushasthana/Documents/Tutedude course/python/10_file_handling/preactice.txt"
# if os.path.exists(file_name):
#     print("file exists") #file exists
# else:
#     print("file does not exist") #file does not exist


#pathlib.path.exsits()
from pathlib import Path
# file_name = Path("/Users/piyushasthana/Documents/Tutedude course/python/10_file_handling/preactice.txt")
file_name = Path("/Users/piyushasthana/Documents/Tutedude course/python/10_file_handling/preactic.txt")
if file_name.exists():
    print("file exists,cannot create!") #file exists
else:
    print("file does not exist, creating the file") #file does not exist
    f = open("preactic.txt",'xt')
    f.write("new file has been created")
    f.close()