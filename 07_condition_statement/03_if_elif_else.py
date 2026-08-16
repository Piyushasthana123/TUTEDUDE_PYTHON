"""
>= 90 ,grade A
80 and 89 , grade B
70 and 79 , grade C
60 and 69 , grade D
< 60 , grade F
"""
number = int(input("Enter a number: "))
if number >= 90:
    print(f"the student got {number} is have grade A")
elif 80 <= number < 90:
    print(f"the student got {number} is have grade B")
elif  number >=70 and number < 80:
    print(f"the student got {number} is have grade C")
elif  number >=60 and number <70:
    print(f"the student got {number} is have grade D")
else:
    print(f"the student got {number} is grade F")