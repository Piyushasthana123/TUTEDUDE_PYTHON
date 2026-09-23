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

# c1 = PhoneBook('c1',52349835748490)
# c2 = PhoneBook('c2',9878943752349)
# print(c1.Phone_directory)
# print(c1.show_contact())
# print(c2.show_contact())
PhoneBook.show_all_contact()