import random
class user:
    def __init__(self,name,email,account_type)-> None:
        self.name=name
        self.email=email
        self.account_type=account_type
        self.account_number=random.randint(12134260,22134260)
        self.transaction=[]
        self.loan=0
        self.lbalance=0
        self.balance=0


    def __repr__(self) -> str:
        return f'user information\n------------------\nname  : {self.name}\naccount number  : {self.account_number}\nbalance  : {self.balance}\nemail : {self.email}\n'
    
class Admin:
    def __init__(self,name,id,passward,email) -> None:
        self.name=name
        self.id=id
        self.passward=passward
        self.email=email
    
    def __repr__(self) -> str:
        return f'Admin information\n------------------\nname  : {self.name}\nID number  : {self.id}\nemail : {self.email}'
    



class bank:
    def __init__(self,name) -> None:
        self.name=name
        self.users=[]
        self.admin=[]
        self.loan_feature=True
        self.balance=100000
        self.bankrupt=False
        

    
    def create_account(self,holder):
        self.users.append(holder)
        print(f"{holder.name} Account Number is {holder.account_number}")

    
    def all_accounts_list(self):
        print(user.account_number for user in self.users)

    def deposit(self, account_number, amount):
        for user in self.users:
            if user.account_number== account_number:
                user.balance+=amount
                user.transaction.append(f"Deposited: {amount}")
                self.balance+=amount
                return f"Deposited {amount} successfully"
        return "Account not found"
    
    def withdraw(self, account_number, amount):
        if not self.bankrupt and amount<=self.balance:
            for user in self.users:
                if user.account_number == account_number:
                    if user.balance >= amount  :
                        self.balance-=amount
                        user.balance -= amount
                        user.transaction.append(f"Withdrew: {amount}")
                        return f"Withdrew {amount} successfully"
                    else:
                        return "Withdrawal amount exceeded"
            return "Account not found"
        else:
            return "Bank is bankrupt, withdrawals are not allowed"
    
    def Transiction_history(self,account_number):
        
        for user in self.users:

            if user.account_number ==account_number:
                print("\nTransaction History\n------------------")
                for i in user.transaction:
                    print(i)
    

    def take_loan(self, account_number, amount):
        if not self.bankrupt:
            if self.loan_feature:
                max_loan_amount=(self.balance)
                for user in self.users:
                    if user.account_number == account_number:
                        if user.loan < 2:
                            if amount <= max_loan_amount:
                                user.loan += 1
                                user.lbalance += amount
                                user.balance += amount
                                user.transaction.append(f"Loan taken: {amount}")
                                self.balance -= amount
                                return f"Loan of {amount} taken successfully {user.account_number}"
                            else:
                                return f"Loan amount exceeds the maximum limit of {max_loan_amount}"
                        else:
                            return "Maximum number of loans taken"
                return "Account not found"
            else:
                return "Loan feature is currently inactive"
        else:
            return "Bank is bankrupt, loans are not allowed"
        
    
    def ALL_user(self):
        
        for user in self.users:
            print(user)
    
    
    def delete_account(self, account_number):
        for user in self.users:
            if user.account_number == account_number:
                self.users.remove(user)
                return f"Account {account_number} deleted successfully"
        return "Account not found"
    

    def transfer_amount(self, from_account_number, to_account_number, amount):
        user1 = None
        user2 = None

        for user in self.users:
            if user.account_number == from_account_number:
                user1 = user
            if user.account_number == to_account_number:
                user2 = user

        if user1 and user2:
    
            if user1.balance >= amount:
                user1.balance -= amount
                user2.balance += amount
                user1.transaction.append(f"Transferred {amount} to account number {to_account_number}")
                user2.transaction.append(f"Received {amount} from account number {from_account_number}")
                return f"Transferred {amount} to account number {to_account_number} successfully"
            
            else:
                return "Insufficient funds for transfer"
        else:
            return "Account does not exist"


    def total_balance(self):
        total = self.balance
        return total

    def total_loan_amount(self):
        total_loan = sum(user.lbalance for user in self.users)
        return total_loan

    def add_Admin(self,admin):
        self.admin.append(admin)

    def information(self,account):
        for user in self.users:
            if user.account_number==account:
                print(user)
                return
        
        return f"Account {account} not found "
    
    
    def bankrupt(self):
        if self.balance<=0:
            self.bankrupt=True

        else:
            self.bankrupt=False

    



        

sonali=bank("sonali")

#admin

Admin1=Admin("Romjan",2101017,'1234',"romjan@gmail.com")
Admin2=Admin("Ifty",2101014,'4321',"ifty@gmail.com")
Admin3=Admin("Atik",2101040,'2341',"Atik@gmail.com")

#user
user1=user("zunaid","zunaid@gmail.com",'s')
user2=user("Atik","Atik@gmail.com",'s')
sonali.create_account(user2)
sonali.create_account(user1)

sonali.add_Admin(Admin1)
sonali.add_Admin(Admin2)
sonali.add_Admin(Admin3)




currentUser=None
while True:
    if currentUser==None:
        print("----Assalamualykum-----")
        print(" ")

        option=input("Login or Register(L/R) \nExit(E)")
        


        if option=='L':
           
            option2=input("1.Login as Admin\n2.Login as user\n")

            if(option2=='1'):
                Id=int(input("Enter id :"))
                Password=input("Enter password :")
                
                match=False
                for i in sonali.admin:
                    if  i.id==Id and i.passward==Password:
                        print(f"\nWELLCOME MR {i.name}\n------------------")
                        currentUser=i
                        match=True
                        break
                if match==False:
                    print("Wrong ID OR PASS ")
            
            elif(option2=='2'):
                ac=int(input("Enter Account Number"))
                for user in sonali.users:
                    match=False
                    if user.account_number ==ac:
                        print(f"\nWELLCOME MR {user.name}\n------------------")
                        currentUser=user
                        match=True
                        break
                if match==False:
                    print("Wrong Account Number ")    
    

        elif option=='R':
            
            Name=input("Enter name :")
            Email=input("Enter Email :")
            AT=input("Enter Account Type\nfor Saving press s for current account press c:")
            user1=user(Name,Email,AT)
            sonali.create_account(user1)
            currentUser=user1
            print(f"\nWELLCOME MR {user1.name}\n------------------")

        elif option=='E':
            break



    
    else:
        if currentUser in sonali.admin:
            print("1.create an user account \n2.delete any user account\n3.all user accounts list\n4.Total available balance of the bank.\n5.total loan amount.\n6.on or off the loan feature of the bank\n7.Exit")
            ch=(input("Enter option "))
            
            if ch=='1':
                Name=input("Enter name :")
                Email=input("Enter Email :")
                AT=input("Enter Account Type\nfor Saving press s for current account press c:")
                user1=user(Name,Email,AT)
                sonali.create_account(user1)

            
            elif ch=='2':
                AC=int(input("Enter Account Number  :"))

                print(sonali.delete_account(AC))

            elif ch=='3':
                sonali.ALL_user()

            elif ch=='4':
                print(f'total balance of the bank is {sonali.total_balance()}')

            elif ch=='5':
                print(f'total balance of the bank is {sonali.total_loan_amount()}')

            elif ch=='6':
                print(f"Loan feature {sonali.loan_feature}")

                ch=input("Update Loan feature (Y/N)")
                
                if ch=='Y':
                    sonali.loan_feature=True
                    print("Loan feature ON")
                
                elif ch=='N':
                    sonali.loan_feature=False
                    print("loan feature OFF") 
                



            elif ch=='7':
                currentUser=None

        elif currentUser in sonali.users:
            print("1.Deposit \n2.Wthdraw \n3.Check information \n4.Transaction History.\n5.Take Loan \n6.Transfer balance \n7.Exit")

            ch=(input("Enter option "))

               
                
            if ch=='1':
                amount=int(input("enter amount"))

                print(sonali.deposit(currentUser.account_number,amount))

            elif ch=='2':
                
                amount=int(input("enter amount"))

                print(sonali.withdraw(currentUser.account_number,amount))


            elif ch=='3':
                
                sonali.information(currentUser.account_number)


            elif ch=='4':
                sonali.Transiction_history(currentUser.account_number)


            elif ch=='5':
                amount=int(input("enter amount"))
                print(sonali.take_loan(currentUser.account_number,amount))
                

            elif ch=='6':

                ac=int(input("Please type account for sending money"))
                amount=int(input("enter amount"))
                sonali.transfer_amount(currentUser.account_number,ac,amount)

            elif ch=='7':
                currentUser = None

