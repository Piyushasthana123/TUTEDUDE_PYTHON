import re
# sub()
days = "Sunday ,monday , tuesday , monday , thursday , Sunday,Saturday"
# pat = "sunday"
pat = r"S[a-z]+"
replaced = "friday"
result = re.sub(pat,replaced,days) # friday ,monday , tuesday , monday , thursday , friday
# result = re.sub(pat,replaced,days,count= 1) # friday ,monday , tuesday , monday , thursday , sunday
print(result) #friday ,monday , tuesday , monday , thursday , friday,friday

message ="""we are learning re module . using RE ,we can search for a pattern in a given string. using the 
sub() , we can replace the pattern with the given string as well """
pat = r"\bre\b"
replaced = "regular Expression"
# result = re.sub(pat,replaced,message)
result = re.sub(pat,replaced,message,flags=re.IGNORECASE)
print(result)
# we are learning regular Expression module . using regular Expression ,we can search for a pattern in a given string. using the
# sub() , we can replace the pattern with the given string as well

phone = "+91-389264982349 , +91-2093204123409"
pat = r"[+-]"
replaced = ""
result = re.sub(pat,replaced,phone)
print(result) #91389264982349 , 912093204123409
