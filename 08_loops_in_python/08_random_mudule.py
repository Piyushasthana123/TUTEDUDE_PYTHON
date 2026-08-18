import random

#random() -returns random float value btw 0.0 and 1.0(excluded)
# print(random.random()) # 0.541182225824976

#randint(a,b)- returns random integers btw a and b (both included)
# print(random.randint(1,100))

# num =[10,4,1,8,4,3]
fruits = ['apple', 'banana', 'orange']
#choice(sequences) => returns random item from the sequences
# dd=random.choice(num)
# dd=random.choice(fruits)
# print(dd)

#shuffle(sequences) =>returns the elements shuffled in random order
print(random.shuffle(fruits)) #None
print(fruits) #shuffled list is ['orange', 'banana', 'apple']