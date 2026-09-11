#Regular Expression(RegEx) - RE module
import re
message= "the current version of python is 3.13 , other previous version is 3.12 , 3,11, 3.10."

"""
#if python is present in message
print('python' in message )
print('13' in message )
print('14' in message )
print(message.find('3.13')) #33
print(message.find('python')) #23
"""

"""
re.search(RegEx_pattern,string) => return a match object when there is match found, else return None 

output match
<re.Match object; span=(35, 37), match='13'>
found!!

output not match
None
not found!!
"""

match_obj = re.search('13',message)
print(match_obj)

if re.search('13',message):
    print('found!!')
else:
    print('not found!!')
print(message[35 : 37])