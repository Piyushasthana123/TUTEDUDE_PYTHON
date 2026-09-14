import re
with open("student_detailes",'rt')as f:
    data = f.read()
# pat = r"[a-zA-Z]+[a-zA-Z0-9_.-]+[@][a-z]+[.][]a-z]+"
# pat = r"\b[a-zA-Z]+[\w.-]+[@][a-z]+[.][]a-z]+\b"
pat = r"\b[a-zA-Z]+[\w.-]+[@][a-z]+[.][]a-z]{2,}\b"
matches_obj = re.finditer(pat,data)
for match in matches_obj:
    print(match)
"""
<re.Match object; span=(6, 33), match='alice-cool_231@mydomain.com'>
<re.Match object; span=(51, 76), match='john.dan.1234@example.com'>
<re.Match object; span=(94, 116), match='carol_1234@mydomain.in'>
"""