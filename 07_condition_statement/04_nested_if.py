"""
if marks is >= 60 , student  is pass else student is fail
and the student is pass , then we print the grade
   >= 90 ,grade A
   80 and 89 , grade B
   70 and 79 , grade C
   60 and 69 , grade D
   < 60 , grade F
"""
number = int(input("Enter a number: "))
if number >=60:
    print(f"the student is is pass the Exam by {number} marks")
    if number >= 90:
        print(f"the student got {number} marks with grade A")
    elif 80 <= number < 90:
        print(f"the student got {number} marks with grade B")
    elif  number >=70 and number < 80:
        print(f"the student got {number} marks with grade C")
    else:
        print(f"the student got {number} marks with grade D")
else:
    print(f"the student is fail the Exam by {number} marks with grade F")