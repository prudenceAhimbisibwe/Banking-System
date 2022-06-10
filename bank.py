class Account:
     def __init__(self,account_number,account_name):
        self.account_number=account_number
        self.account_name=account_name
        self.balance=0
        self.deposits=[]
        self.withdraws=[]
        self.withdraw_charge=100
        

     def deposit(self,amount):
        if amount<=0:
            return f"Deposit must be positive amount"
        else:
            self.balance+=amount
            self.deposits.append(amount)
            print (self.diposits)
            return f"Hello, {self.account_name} you have deposited KES{amount} your new balance is KES{self.balance}"

     def withdraw(self,amount):
        if amount<=0:
            return f"withdraw should be greater than zero"
        elif amount>self.balance:
            return f"your balance is {self.balance},you can't withdraw KES{amount}"
        elif amount-self.withdraw_charge:
            return f"KES {self.withdraw_charge} has been deducted for the withdraw charges"
        else:
            self.balance-=amount
            self.withdraws.append(amount)
            print (self.withdraw)
            return f"Hello, {self.account_name}you have withdrawn KES{amount} and your new balance is KES{self.balance}"

     def deposits_statement(self):
        for y in self.deposit:
            print (y,end="\n")

     def withdrawals_statement(self):
        for x in self.withdraw:
            print (x,end="\n")

     def current_balance(self):
        return f"Your current balance is KES{self.balance}"




