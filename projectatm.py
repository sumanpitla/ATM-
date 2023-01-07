import json
class ATM:
    def __init__(self,name,ac_no,balance=0):
        self .name=name
        self.ac_no=ac_no
        self.balance=balance

    def account_details(self):
        print("<<<<<<<<account details >>>>>>>")
        print("account holder name:",self.name)
        print("acoount number:",self.ac_no)
        print("acount balance:",self.balance)
        self.transaction()
    def check_balance(self):
        print("ACCOUNT BALANCE:",self.balance)
        self.transaction()
    def account_deposite(self):
        dep_amount=int(input("enter the deposite amount:"))
        self.balance=dep_amount+self.balance
        dic[name]['Balance'] = self.balance
        print("\AFTER DEPOSIT AMOUNT IN THE ACOUNT:/")
        print("acount balance:", self.balance)
        self.transaction()
    def withdraw(self):
        w_amount=int(input("Enter withdraw amount:"))
        if w_amount>self.balance:
            print("Not possible to withdraw !!!,you have not sufficient balance")
            print("current balance:",self.balance)
        else:
            self.balance=self.balance-w_amount
            print("remaining balance:",self.balance)
        self.transaction()


    def transaction(self):
        print("""
                   TRANSACTION 
               *********************
                   Menu:
                   1. Account Detail
                   2. Check Balance
                   3. Deposit
                   4. Withdraw
                   5. Exit
               *********************
               """)

        option=int(input("Enter 1,2,3,4 or 5:"))
        if option==1:
            a.account_details()
        elif option==2:
            a.check_balance()
        elif option==3:
            a.account_deposite()
        elif option==4:
            a.withdraw()
        elif option==5:
            print(""" >>>>>>>>>>>RECIEPT<<<<<<<<<<<<
            *******TRANSACTION DETAILS*****""")
            print("account holder name:",self.name)
            print("acoount number:",self.ac_no)
            print("acount balance:",self.balance)
            print("_______THANKs FOR CHOOSING OUR BANK________")
        else:
            print("Wrong selection,select only in 1,2,3,4,5")
            self.transaction()




print("------WELCOME TO SBI ATM -------")
print("_______check your account staus to fill below details______")
name=input("enter full name:")
account_number=input("enter account number:")
print("successfully created your account in sbi bank. ")
a=ATM(name,account_number)


dic = {
    name: account_number
}
with open('db.json', 'a+') as db:
    json.dump(dic, db)
db.close()

print("Do you want to do any transactions ?")
ans=input("enter here yes or no:")

if ans=="yes":
    a.transaction()
elif ans=="no":
    print("_______THANKs FOR CHOOSING OUR BANK________")
else:
    print("Sakkaga kotta raaaaa")
    ans = input("enter here yes or no:")


