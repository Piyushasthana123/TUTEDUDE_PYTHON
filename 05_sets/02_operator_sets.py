student1 = {"English", "Maths", "History","physics","chemistry"}
student2 = {"English", "Hindi", "cs","biology","chemistry","physics"}
student3 = {"sanskrit","g.k","cs","Maths"}
#common subjects of student1 and student2 - intersection
# common_subjects= student1.intersection(student2)
# common_subjects = student1 & student2
# print(common_subjects) #{'physics', 'English', 'chemistry'}

# all subjects of student1 and student2 - union,|
# all_subjects = student1.union(student2)
# all_subjects = student1|student2
# print(all_subjects) #{'Hindi', 'English', 'cs', 'biology', 'physics', 'History', 'chemistry', 'Maths'}
# all_subjects = student1.union(student2,student3)
# all_subjects = student1|student2|student3
# print(all_subjects)
#{'English', 'Maths', 'chemistry', 'cs', 'History', 'Hindi', 'biology', 'g.k', 'physics', 'sanskrit'}

# common subject btw student1 ,student2 and student3 - intersection
# common_subjects = student1.intersection(student2,student3)
# print(common_subjects) #set() empty set

days ={"mon","tue","wed","thur","fri","sat","sun"}
weekends ={"sat","sun"}

#DIFFERENCE OF SETS
# weekdays = days - weekends #elements of days which are NOT in weekends
# weekdays = days.difference(weekends)
# print(weekdays) #{'mon', 'wed', 'fri', 'tue', 'thur'}
