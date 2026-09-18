# Attribute

class Students:
    pass
s1 = Students()
s2 = Students()

s1.name = "jhon"
s2.roll = 1001
print(s1.name) # jhon
print(s2.roll) # 1001

print(s1.__dict__) # {'name': 'jhon'}

