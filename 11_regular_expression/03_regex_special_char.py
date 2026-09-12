import re
s1 = "Python is a programming language.python3.13 is the current version"

# [A-Z],[a-z]

# pat = r"[A-Z][a-z][a-z]"
# pat = r"old \new"
# print(pat) #old \new

# match_obj = re.search(pat,s1)
# print(match_obj) #<re.Match object; span=(0, 3), match='Pyt'>

#\d and \D
#\d  => match only 1 digit character. It is similar to [0-9]
# pat = r"[a-z][a-z][a-z]\d"
# match_obj = re.search(pat,s1)
# print(match_obj) #<re.Match object; span=(36, 40), match='hon3'>

# \D => matches 1 non-digit character.It is similar to [0-9]
pat = r"[a-z][a-z][a-z]\D"
match_obj = re.search(pat,s1)
print(match_obj) #<re.Match object; span=(1, 5), match='ytho'>

#\s ,\S
#\s => matches any whitespace character, tab and new line character
pat = r"[a-z][a-z][a-z]\s"
match_obj = re.search(pat,s1)
print(match_obj)#<re.Match object; span=(3, 7), match='hon '>

s2 = """hi there 
we are learning python 
"""
pat = r"[a-z][a-z][a-z]\s"
match_obj = re.search(pat,s2)
print(match_obj) #<re.Match object; span=(2, 6), match='llo '> or <re.Match object; span=(5, 9), match='ere '>

# \S => opposite of \s . It matches any character except , space , \n  and \t
pat = r"[a-z][a-z][a-z]\S"
match_obj = re.search(pat,s2)
print(match_obj) #<re.Match object; span=(3, 7), match='ther'>

#\w => matches [a-z][A-Z][0-9]
pat = r"[a-z][a-z][a-z]\w"
match_obj = re.search(pat,s2)
print(match_obj) #<re.Match object; span=(3, 7), match='ther'>

#\W => opposite of \w. matches a character except - [a-z][A-Z][0-9].
pat = r"[a-z][a-z][a-z]\W"
match_obj = re.search(pat,s2)
print(match_obj) #<re.Match object; span=(5, 9), match='ere '>