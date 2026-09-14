import re
phone = "alice - 123234243545, mark - 908745476897 , carol - 234684723402"

pat = r"\d{10}"

pat_compile = re.compile(pat)
print(pat_compile)
print(type(pat_compile))

match_obj= re.findall(pat_compile,phone)
print(match_obj)#['1232342435', '9087454768', '2346847234']

with open ("student_detailes",'rt') as f:
    data = f.read()
print(data)
print(type(data))
phone_matches =re.finditer(pat_compile,data)
print(phone_matches)
for match in phone_matches:
    print(match)

# <callable_iterator object at 0x103204130>
# <re.Match object; span=(24, 34), match='9730947230'>
# <re.Match object; span=(58, 68), match='2983412984'>

"""
Alice alice@example.com 97309472309
john john@example.com 2983412984
carol carol@eample.com 234907240

<class 'str'>
"""

