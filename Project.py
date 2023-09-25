from Validations import *
class Bank:
    BankDict={}
    def __init__(self,banknm,ifsc,accno,account_holder_name,age,gender,dob,address,city,type_acc,bal,pancard,adharcard):
        self.banknm=banknm
        self.ifsc=ifsc
        self.accno=accno
        self.account_holder_name=account_holder_name
        self.age=age
        self.gender=gender
        self.dob=dob
        self.address=address
        self.city=city
        self.type_acc=type_acc
        self.bal=float(bal)
        self.pancard=pancard
        self.adharcard=adharcard
        if self.type_acc in self.BankDict.keys():
            self.BankDict[self.type_acc].append(self.account_holder_name)
        else:
            self.BankDict[self.type_acc]=[self.account_holder_name]

    def Display_details(self):
        print("Bank name:",self.banknm)
        print("IFSC code:",self.ifsc)
        print("Account number:",self.accno)
        print("Account Holders Name:",self.account_holder_name)
        print("Age:",self.age)
        print("Gender is:",self.gender)
        print("Date of Birth is:",self.dob)
        print("Address is:",self.address)
        print("City is:",self.city)
        print("Type of Account is:",self.type_acc)
        print("Available Balance is:",self.bal)
        print("Pancard number is:",self.pancard)
        print("Adharcard Number is:",self.adharcard)
    
    def update_name(self,new_name):
        if isNameValid(new_name):
            self.account_holder_name=new_name
            return True
        else:
            return False
        
    def update_address(self,new_address):
        if isaddValid(new_address):
            self.address=new_address
            return True
        else:
            return False
    
    def update_dob(self,new_dob):
        if isdobValid(new_dob):
            self.dob =new_dob
            return True
        else:
            return False 

    def deposit(self,accno ,amount):
        if amount>0:
            if self.accno == accno:
                self.bal= int(self.bal) + amount
                print("Deposit of {amount} successfull, New balance: {self.bal}")
                return True
            else:
                print("Invalid account number!!")
        else:
            print("Invalid amount for deposit")
        return False
        
    def withdraw(self,accno, amount):
        if amount>0 and self.bal >=amount:
            self.bal -= amount
            return True
        else:
            return False
        
        
    def transfer_funds(self,account,amount):
        if amount>0 and self.bal>=0:
            self.bal=self.bal-amount
            account.bal=account.bal+amount
            return True
        else:
            return False


    def balance_enquiry(self):
        print(self.bal)



BankList=[]
print("")
print("Banking operation System")
while True:
    print("")
    print("1.Create Account")
    print("2.Display Details")
    print("3.Update Account Details")
    print("4.Deposit")
    print("5.Withdraw")
    print("6.Funds Transfer")
    print("7.Search the details of Account Holder")
    print("8.Balance Enquiry")
    print("9.Delete Account")
    print("10.Exit")
    choice=int(input("Enter your choice"))

    if choice==1:
        while True:
            banknm=input("Enter Bank Name:")
            if(isNameValid(banknm)):
                break
            else:
                print("Invalid name!!!")
        
        while True:
            ifsc=input("Enter the ifsc code:-")
            if(isifscValid(ifsc)):
                break
            else:
                print("Please Enter the ifsc code in proper format")

        while True:
            accno=input("Enter the Account number")
            if(isaccValid(accno)):
                break
            else:
                print("Invalid Account number!!!")

        while True:
            account_holder_name=input("Enter the Account holder name:")
            if(isNameValid(account_holder_name)):
                break
            else:
                print("Invalid Account holder name!!!")

        while True:
            age=input("Enter your Age:")
            if(isAgeValid(age)):
                break
            else:
                print("Invalid Age!!")

        while True:
            gender=input("Enter your gender")
            if(isGenderValid(gender)):
                break
            else:
                print("Please enter a valid Gender!!")

        while True:
            dob=input("Enter your Date of Birth:")
            if(isdobValid(dob)):
                break
            else:
                print("Invalid Date of Birth!!!")

        while True:
            address=input("Enter your Address:")
            if(isaddValid(address)):
                break
            else:
                print("Please enter a valid Address!!")

        while True:
            city=input("Enter your City:")
            if(iscityValid(city)):
                break
            else:
                print("Please enter a valid City name!!!")

        while True:
            type_acc=input("Please enter your type of account:")
            if(istypeValid(type_acc)):
                break
            else:
                print("Invalid!!Please enter a valid Account Type!!")

        while True:
            bal=input("Enter Balance:")
            if(isbalValid(bal)):
                break
            else:
                print("Invalid!!")

        while True:
            pancard=input('Enter your Pancard number:')
            if(ispanValid(pancard)):
                break
            else:
                print("Please enter a valid Pancard number!!!")

        while True:
            adharcard=input("Enter your Adharcard number")
            if(isadharValid(adharcard)):
                break
            else:
                print("Please enter a valid Adharcard number!!!")

        acc=Bank(banknm,ifsc,accno,account_holder_name,age,gender,dob,address,city,type_acc,bal,pancard,adharcard)
        BankList.append(acc)
    
    elif(choice==2):
        for i in BankList:
            i.Display_details()

    elif(choice==3):
        print("")
        print("Press A to Update name of Account Holder")
        print("Press B to Update address of Account Holder")
        print("Press C to Update DOB of Account Holder")
        ch=input("Enter your choice:-")
        if ch=='A':
            account_number=input("Enter the account number to update name:")
            for acc in BankList:
                if acc.accno ==account_number:
                    new_name=input("Enter the new name:")
                    if acc.update_name(new_name):
                        print("Name Updated Successfully!!")
                    else:
                        print("Invalid name!!")
        
        elif ch=='B':
              account_number=input("Enter the account number to update name:")
              for acc in BankList:
                if acc.accno ==account_number:
                    new_address=input("Enter the new Address:")
                    if acc.update_address(new_address):
                        print("Address updated successfully!!")
                    else:
                        print("Invalid Address!!")

        elif ch=='C':
            account_number=input("Enter the account number to update name:")
            for acc in BankList:
                if acc.accno ==account_number:
                    new_dob=input("Enter the new Date of Birth:")
                    if acc.update_dob(new_dob):
                        print("Date of Birth updated successfully!!")
                    else:
                        print("Invalid date of birth!!")

        else:
            print("Invalid choice for Updation! Plase select a valid Choice!")


    elif(choice==4):
        account_number=input("Enter the account number to deposit:-")
        deposit_amount=float(input("Enter the amount to be deposited:-"))
        for acc in BankList:
            if acc.accno == account_number:
                if acc.deposit(account_number,deposit_amount):
                    print("Deposit Successfull",acc.balance_enquiry())
                else:
                    print("Deposit failed!!")
                break
            else:
                print("Account not found!!")

    elif(choice==5):
       account_number=input("Enter the account number to be withdrawn:-")
       withdraw_amount=float(input("Enter the amount to be withdrawn:-"))
       for acc in BankList:
            if acc.accno == account_number:
                if acc.withdraw(account_number,withdraw_amount):
                    print("Withdraw Successfull",acc.balance_enquiry())
                else:
                    print("Withdraw failed!!")
                break
            else:
                print("Account not found!!")

    elif(choice==6):
        account1=input("Enter the first account number")
        account2=input("Enter the second account number")
        amount=float(input("Enter the amount you want to transfer:-"))

        acc1_exists=False
        acc2_exists=False  

        for acc in BankList:
            if acc.accno == account1:
                acc1_exists=True
            elif acc.accno == account2:
                acc2_exists=True

        if acc1_exists and acc2_exists:
            for acc in BankList:
                if acc.accno == account1:
                    sender=acc
                elif acc.accno == account2:
                    account=acc

            if sender.transfer_funds(account,amount):
                print("Funds Transfer Successfull!!")
                print("New Balance for sender",sender.bal)
                print("New Balance for another account who received:",account.bal)
            else:
                print("Funds transfer Failsed!!!. Insuffeicient balance or Invalid Amount")
        else:
            print("One or both accounts do not exist!!")

    elif(choice==7):
        print("")
        print("Press A to search by Account Number")
        print("Press B to search by Name")
        print("Press C to search by Account Type")
        ch=input("Enter your choice:")
        if(ch=='A'):
            a=int(input("Enter the Account number to be searched:"))
            for i in BankList:
                if i.accno==a:
                    i.Display_details()
        elif(ch=='B'):
            name=input("Enter name to be searched:")
            for i in BankList:
                if i.account_holder_name==name:
                    i.Display_details()
        elif(ch=='C'):
            type=input("Enter the type of account to be searched:")
            for i in BankList:
                if i.type_acc==type:
                    i.Display_details()
        else:
            print("Invalid Choice!!!")
    
    elif(choice==8):
        for i in BankList:
            acc.balance_enquiry()

    elif(choice==9):
        accountno=input("Enter te account number to delete")
        flag = True
        for i in BankList:
            if i.accno == accountno:
                flag = False
                BankList.remove(i)
                break
        if flag:
            print("Not found ")
            

    elif(choice==10):
        print("Exit")
        break
