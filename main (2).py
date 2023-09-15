#Implement a class called BankAccount that represents a bank account. The class should have private attributes for account number, account holder name, and account balance. Include methods to deposit money, withdraw money, and display the account balance. Ensure that the account balance cannot be accessed directly from outside the class. Write a program to create an instance of the BankAccount class and test the deposit and withdrawal functionality.

class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Welcome to Deposit & Withdrawal Machine!")
        
    def deposit(self):
        amount=float(input("Enter amount to be deposited: "))
        self.balance += amount
        print("Amount Deposited: ",amount)
    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if self.balance>=amount:
            self.balance-=amount
            print("You withdraw: ",amount)
        else:
            print("Insufficient balance ")
    def display(self):
        print("Net Available Balance=",self.balance)
#creating an object of class
s = Bank_Account()

#calling functions with that class
s.deposit()
s.withdraw()
s.display()
