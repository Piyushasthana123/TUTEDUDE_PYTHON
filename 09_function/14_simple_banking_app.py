balance_amount = 0.0
kyc_document = {}
def check_balance():
    name = input("enter your name: ")
    password = int(input("enter your password: "))
    if name == "piyush" and password == 20089:
        print("=======================================")
        print(f"Hello! {name} your current balance is : {balance_amount}")
        print("=======================================")
    else:
        print(f"your username and pass is invalid!!!")
    return balance_amount
def deposit(amount):
    name = input("enter your name: ")
    password = int(input("enter your password: "))
    if name == "piyush" and password == 20089:
        global balance_amount
        if amount > 0:
            balance_amount += amount
            print("=======================================")
            print(f"deposited  amount is: {amount}")
            print("=======================================")
        else:
            print("amount enter is not  valid amount it should be greater than 0!!!!")
            print("=======================================")

def withdraw(amount):
    name = input("enter your name: ")
    password = int(input("enter your password: "))
    if name == "piyush" and password == 20089:
        global balance_amount
        if 0 < amount <= balance_amount:
            balance_amount -= amount
            print("=======================================")
            print(f"successfully  withdrawing  the amount: {amount}")
            print("=======================================")
        else:
            print("amount should be greater than 0 or less then or equal to balance amount!!!!")
            print("=======================================")
def update_kyc(docs):
    global kyc_document
    kyc_document.update(docs)

def check_kyc(**docs):
    if len(kyc_document) == 0:
        print("kyc is not done yet!!!")
    else:
        for doc in kyc_document:

            print(f"{doc} : {kyc_document[doc]}")
            print("=======================================")


if __name__=="__main__":
    print("=======================================")
    print("welcome to ABC bank service ")
    print("=======================================")
    print()

    while True:
        print("1. check your balance")
        print("2. Deposit an amount")
        print("3. withdraw an amount")
        print("4. check kyc")
        print("5. update kyc")
        print("6. Exit")
        choice = input("enter your choice (1-6): ")
        print("=======================================")
        if choice == "1":
           balance = check_balance()
        elif choice == "2":
            amount = float(input("enter your amount: "))
            deposit(amount)
        elif choice == "3":
         amount = int(input("enter your amount: "))
         withdraw(amount)
        elif choice == "4":
            check_kyc()
        elif choice == "5":
            kyc_docs = {}
            n_documents = int(input("enter the number of documents you want to add: "))
            for i in range(n_documents):
                print("=======================================")
                key = input("enter the document type: ")
                print("=======================================")
                value = input("enter the document number: ")
                kyc_docs[key] = value
            update_kyc(kyc_docs)
            print("=======================================")
            print("kyc updated successfully!!!")
            print("=======================================")
        elif choice == "6":
            break
        else:
         print("please enter valid choice!!!!")
         print("=======================================")
    print()
    print("thank you for using my bank services")



