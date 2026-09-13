# +
import re
s1 = "Python is a programming language.python3.13 is the current version"
# pat = r"[a-z]{4}"
# match_obj = re.search(pat, s1)
# print(match_obj)


# pat = r"[A-Z][a-z]{4}"
# match_obj = re.search(pat, s1)
# print(match_obj)

#<re.Match object; span=(1, 5), match='ytho'>
# <re.Match object; span=(0, 5), match='Pytho'>

# + => matches 1 or more repetitions of the previous pattern
# pat = r"[A-Z][a-z]+"
# match_obj = re.search(pat, s1)
# print(match_obj)#<re.Match object; span=(0, 6), match='Python'>

# ? => 0 or 1  repetitions of the previous pattern
# pat = r"[A-Z][a-z]?"
# match_obj = re.search(pat, s1)
# print(match_obj) # <re.Match object; span=(0, 2), match='Py'>

# * => 0 or more repetitions of the previous pattern
pat = r"[A-Z][a-z]*"
match_obj = re.search(pat, s1)
print(match_obj) #<re.Match object; span=(0, 6), match='Python'>