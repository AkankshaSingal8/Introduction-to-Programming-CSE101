from datetime import datetime

class BankAccount:
    def __init__(self,username, password, cbalance):
        self.username = username
        self.password = password
        self.balance = cbalance
        u=self.username+".txt"
        f = open(u,'w')
        f.close()
    def authenticate(self):
        pswd = input("Provide your secret password: ")
        if pswd == self.password:
            return(True)
        else:
            return(False)
        
    def deposit(self,amt):
        n=0
        wrong = 0
        while True:
            try:
                if self.authenticate():
                    self.balance += amt
                    u=self.username+".txt"
                    with open(u,'a') as f:
                        tmstmp = str(datetime.now())
                        txt=tmstmp+f" The amount of Rupees {amt} has been added Current balance -> {self.balance}"+'\n'
                        f.write(txt)
                    n += 1
                    break
                else:
                    wrong += 1
                    n += 1
                assert wrong<=2 and n<=3
            except AssertionError:
                print("Too many wrong attempts!!")
                break
            
                   
        
    def withdraw(self,amt):
        n=0
        wrong = 0
        while True:
            try:
                if self.authenticate():
                    if amt < self.balance:
                        self.balance -= amt
                        u=self.username+".txt"
                        with open(u,'a') as f:
                            tmstmp = str(datetime.now())
                            txt=tmstmp+f" The amount of Rupees {amt} has been debited Current balance -> {self.balance}"+'\n'
                            f.write(txt)
                    else:
                        print("Low balance!! Cannot be debited at this time!")
                        return
                    n += 1
                    break
                else:
                    wrong += 1
                    n += 1
                assert wrong<=2 and n<=3
            except AssertionError:
                print("Too many wrong attempts!!")
                break
            
    def bankStatement(self):
        n=0
        wrong = 0
        while True:
            try:
                if self.authenticate():
                    print(f"Hey {self.username}! Your transaction history:\n")
                    u=self.username+".txt"
                    with open(u,'r') as f:
                        for i in f.readlines():
                            print(i)
                        
                    n += 1
                    break
                else:
                    wrong += 1
                    n += 1
                assert wrong<=2 and n<=3
            except AssertionError:
                print("Too many wrong attempts!!")
                break

print("Welcome to the bank of IIIT-D!\n")
nm = input("Enter name: ")
pswd = input("Enter password: ")
cur = float(input("Starting balance for your account: "))
bank = BankAccount(nm,pswd,cur)
rep ='y'
while rep == 'y':
    print("Select your option:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Bank Statement")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        amt = float(input("Provide the amount to be deposited: "))
        bank.deposit(amt)
    elif ch == 2:
        amt = float(input("Provide the amount to be withdrawn: "))
        bank.withdraw(amt)
    elif ch == 3:
        bank.bankStatement()
    rep = input("Do you wish to continue? (y/n): ")
        
        
