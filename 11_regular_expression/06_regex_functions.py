# match() - only apply  at the Bignig of the string
import re

# s1 = "We are learning regex in python"
# # pat = r"[A-Z][a-z]"
# pat = r"[a-z]{3}"
# print(re.match(pat,s1)) # None

# phone = "john-8372273423, carlo-3204723573 , marks-2394823740"
# pat=r"[0-9]{10}"
# print(re.search(pat,phone)) # <re.Match object; span=(5, 15), match='8372273423'>

#findall()
phone = "john-8372273423, carlo-3204723573 , marks-2394823740 alice-2348238 robert-2343453534905034234234324"
pat=r"[0-9]{10}"
print(re.findall(pat,phone)) # ['8372273423', '3204723573', '2394823740']


pat=r"[0-9]+"
print(re.findall(pat,phone)) # ['8372273423', '3204723573', '2394823740', '2348238']

# fetch all phone numbers. the phone number are exactly 7 digits and should not exceed 15 digits

pat=r"[0-9]{7,15}"
print(re.findall(pat,phone)) #['8372273423', '3204723573', '2394823740', '2348238', '23434535349050']

# fetch all phone numbers. the phone number are atleast 7 digits and more

pat=r"[0-9]{7,}" # 7 or more
print(re.findall(pat,phone)) #['8372273423', '3204723573', '2394823740', '2348238', '2343453534905034234234324']

#\b- boundary
pat=r"[0-9]{7,15}\b" #exactly 15 have taken not more than that
print(re.findall(pat,phone)) #['8372273423', '3204723573', '2394823740', '2348238', '905034234234324']

#finditer()
pat=r"[0-9]{7,15}\b"
match_obj_iterator = re.finditer(pat,phone) #<callable_iterator object at 0x103914520>
for iter in match_obj_iterator:
    print(iter )
# <re.Match object; span=(5, 15), match='8372273423'>
# <re.Match object; span=(23, 33), match='3204723573'>
# <re.Match object; span=(42, 52), match='2394823740'>
# <re.Match object; span=(59, 66), match='2348238'>
# <re.Match object; span=(84, 99), match='905034234234324'>
