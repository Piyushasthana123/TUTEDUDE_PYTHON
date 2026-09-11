# raise

# salary = int(input("Enter your salary: "))
# if salary < 0:
#     raise ValueError("Your salary cannot be negative")
# else:
#     print(f"your salary is {salary} ")
#  raise ValueError("Your salary cannot be negative")
# ValueError: Your salary cannot be negative


age= int(input("Enter your salary: "))
if age < 0:
    raise Exception("Age cannot be negative") # all exception are handle by Exception 
    # raise ValueError("Age cannot be negative")
#raise ValueError("Age cannot be negative")
# ValueError: Age cannot be negative
else:
    if age>= 18 :
        print("you can vote")
    else:
        print("you can not vote")