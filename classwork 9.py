# 1.Create a class named Circle with an attribute radius. Use a constructor to initialize the radius by accepting input from the user. Define the following methods:
#
# class circle:
#     def __init__(self):
#         self.radius=int(input('enter the radious'))
#
#     def getarea(self):
#         print('area',3.14*self.radius**2)
#
#     def getperimeter(self):
#         print('peremeter',2*3.14*self.radius)
#
# c=circle()
# c.getarea()
# c.getperimeter()

# getarea() – to calculate and display the area of the circle.
# getperimeter() – to calculate and display the perimeter (circumference) of the circle.
#
# Create an object of the Circle class and call both methods to display the results.
#
# 2.Create a class named Account with attributes acctnumber, acctname, and balance. Initialize these values using a constructor by taking input from the user. Define the following methods:
#
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
            self.showbalance()

    def deposit(self):
        amount = int(input("Enter the amount to deposit: "))
        self.balance = self.balance + amount
        self.showbalance()


a = Account()

a.withdraw()
a.deposit()
a.showbalance()
# withdraw() – to withdraw an amount from the account and update the balance.
# deposit() – to deposit an amount into the account and update the balance.
# showbalance() – to display the current balance of the account.
#
# Create an object of the class and call the methods to perform withdrawal and deposit operations and display the updated balance
