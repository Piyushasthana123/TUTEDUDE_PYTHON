# filter (function , sequence)
seq = [1,2,3,4,5,6]
# odd = lambda x :True if x % 2 != 0 else False
filtered_output = filter(lambda x :True if x % 2 != 0 else False,seq)
print(filtered_output)
print(f"Odd number in above sequence is : {list(filtered_output)}")
# <filter object at 0x106539f60>
#Odd number in above sequence is : [1, 3, 5]

#map(function , sequence)
mapped_output = map(lambda x :True if x % 2 != 0 else False,seq)
print(mapped_output)
print(f"Odd number in above sequence is : {list(mapped_output)}")
#<map object at 0x10833a260>
# Odd number in above sequence is : [True, False, True, False, True, False]

mapped_output = map(lambda x : x **2,seq)
print(mapped_output)
print(f"Odd number in above sequence is : {list(mapped_output)}")
# <map object at 0x1039024a0>
# Odd number in above sequence is : [1, 4, 9, 16, 25, 36]