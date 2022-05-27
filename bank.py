class Account:
     def __init__(self,account_number,balance,account_name,account_type):
        self.account_number=account_number
        self.account_name=account_name
        self.balance=balance
        self.account_type=account_type

     def deposit(self,amount):
         self.balance+=amount
         return f"Hello, {self.account_name} your new balance is {self.balance}"

     def withdraw(self,amount):
         self.balance-=amount
         return f"Hello, {self.account_name} your new balance is {self.balance}"


