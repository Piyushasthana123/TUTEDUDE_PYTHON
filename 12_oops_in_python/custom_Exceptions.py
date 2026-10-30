# help(Exception)
class SalaryError(Exception):
    pass

def get_salary(salary):
    if(salary < 0):
        raise SalaryEror("Salary can nor be negative!!")
    else:
        bonus = salary * 1.25
        return salary + bonus

salary = int(input('Enter your salary: '))
final_salary = get_salary(salary)
print(final_salary)

####
# Transaction
