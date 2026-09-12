import re
message= "the current version of python is 3.13 , other previous version is 3.12 , 3,11, 3.10."
match_obj = re.search("[0123456789][0-9]",message)
print(match_obj)

match_obj = re.search("[0-9][0-9]","Home number : 251/A")
print(match_obj)
match_obj = re.search("[0-9][0-9][0-9]","Home number : 251/A")
print(match_obj)
"""
<re.Match object; span=(35, 37), match='13'>
<re.Match object; span=(14, 16), match='25'>
<re.Match object; span=(14, 17), match='251'>
"""

# . => matches any character except new line character (\n)
match_obj = re.search("[0-9].[0-9][0-9]",message)
print(match_obj) #<re.Match object; span=(33, 37), match='3.13'>

message_1 = "this year is 2011"
match_obj = re.search("[0-9].[0-9][0-9]",message_1)
print(match_obj) #<re.Match object; span=(13, 17), match='2011'>