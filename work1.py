class Account:
    def __init__(self):
        self.accountnumber = int(input("Enter acc number: "))
        self.acctname = input("Enter your name: ")
        self.balance = int(input("Enter initial balance: "))

    def showbalance(self):
        print("Balance:", self.balance)

    def withdraw(self):
        amount = int(input("Enter the amount to withdraw: "))

        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance = self.balance - amount
            print("Withdrawal successful")
            self.showbalance()

    def deposit(self):
        amount = int(input("Enter the amount to deposit: "))
        self.balance = self.balance + amount
        print("Deposit successful")
        self.showbalance()


l = []

while True:
    print("1. Create a new account")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Show balance")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        a = Account()
        l.append(a)
        print("Account created successfully")

    elif ch == 2:
        number = int(input("Enter account number: "))

        for i in l:
            if i.accountnumber == number:
                i.withdraw()
                break
        else:
            print("Account not found")

    elif ch == 3:
        number = int(input("Enter account number: "))

        for i in l:
            if i.accountnumber == number:
                i.deposit()
                break
        else:
            print("Account not found")

    elif ch == 4:
        number = int(input("Enter account number: "))

        for i in l:
            if i.accountnumber == number:
                i.showbalance()
                break
        else:
            print("Account not found")

    elif ch == 5:
        exit()

    else:
        print("Invalid choice")