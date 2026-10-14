class PhoneBook:
    Phone_directory =[]
    def __init__(self,name,phone_number):
        self.name = name
        self.phone = phone_number
        PhoneBook.Phone_directory.append(self)
    def show_contact(self):
        return f"Name: {self.name}, Contact Number: {self.phone}"

    @classmethod
    def show_all_contact(cls):
        if len(cls.Phone_directory) == 0:
            print("there is no contact found in this directory")
        else:
            for data in  cls.Phone_directory:
                print(data.show_contact())
    @classmethod
    def search_contact(cls,name):
        for data in cls.Phone_directory:
            if data.name == name:
                return f"this is the {data.name} and phone no: {data.phone}"
        return f"{data.name} is not found in present directory"

    @staticmethod
    def valid_Phone_directory(number):
        if len(number) >= 8 and number.isdigit():
            return True
        else:
            return False
n_contact = int(input("how many contact do you want add?: "))
for n in range(n_contact):
    name = input("Enter your name: ")
    phone_number = input("Enter your phone number: ")
    if PhoneBook.validate_,phone_number(phone_number):
        PhoneBook(name,phone_number)


# c1 = PhoneBook('c1',"52349835748490")
# c2 = PhoneBook('c2',"9878943752349")
# c3 = PhoneBook('c3',"52349835748490")
# c4 = PhoneBook('c4',"9878943752349")
# print(c1.Phone_directory)
# print(c1.show_contact())
# print(c2.show_contact())
PhoneBook.show_all_contact()
# PhoneBook.search_contact("c2")