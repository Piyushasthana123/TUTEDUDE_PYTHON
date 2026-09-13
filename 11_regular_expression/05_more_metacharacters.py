
import re
s1 = "python is a programing language"
pat = r"[a-z]{8}"
match_obj = re.search(pat,s1)
print(match_obj) # <re.Match object; span=(12, 20), match='programi'>

# ^ -  caret
pat = r"^[a-z]{8}"
match_obj = re.search(pat,s1)
print(match_obj) #None

# $ - dollar- end of the string
pat = r"[a-z]{8}$"
match_obj = re.search(pat,s1)
print(match_obj) #<re.Match object; span=(23, 31), match='language'>

# group- () + | (or)
email = "abc_123@example.com random worlds and characters. x1y2z3.abc.edu"
pat = r"(com|net|org|edu)"
match_obj = re.search(pat,email)
print(match_obj) # <re.Match object; span=(16, 19), match='com'>