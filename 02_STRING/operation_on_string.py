s1 = "python is fun"
# print(len(s1))
# print(s1[0])
# print(s1[-1])

language = "python"
version="3.13.3"
# this is the concatination in string
# print(language+version)

# star operator is repetetion of string
print(language*3)

# membership operator
# in and not in
print( "python" in language)


"""
comparison operator
==
strip() is use to remove the spaces btw the word

"""
a1="   python  "
# print("python " == "python")
# print(a1.strip() == "python")
s2 = "we are learning Python"
# print(s2.replace("python","java"))
print(s2.replace("e","E",1)) #only 1 replaced by this 'E'


#count operation
print(s2.count("e"))

a2="python"
# changing case of a string
# upper(), lower(),title(),capitalize()
print(a2.upper())
print(a2.lower())
print(s2.capitalize())
print(s2.title())

# starting and ending of a string
print(s2.startswith("w"),s2.endswith("n"))



