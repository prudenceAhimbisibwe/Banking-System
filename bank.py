from datetime import datetime

from requests import request


class Account:
     def __init__(self,account_number,account_name):
        self.account_number=account_number
        self.account_name=account_name
        self.balance=0
        self.deposits=[]
        self.withdrawals=[]
        self.withdraw_charge=100
        self.loan_balance=0
        

     def deposit(self,amount):
        date=datetime.now()
        if amount<=0:
            return f"The amount must be geater than zero"
        else:
            self.balance+=amount
            dep_detail={"date":date.strftime('%d/%m/%y'),"amount":amount,"narration":f"You have deposited {amount} on {date} "}
            self.deposits.append(dep_detail)
            return f"Hello,{self.account_name}{self.deposits}"

     def withdraw(self,amount):
        date=datetime.now()
        total=amount+self.withdraw_charge
        if amount<=0:
            return f"withdraw should be greater than zero"
        elif amount>self.balance:
            return f"your balance is {self.balance},you can't withdraw Ksh {amount}"
        else:
            self.balance-=total
            self.withdrawals.append(amount)
            withdraws_detail={"date":date.strftime('%d/%m/%y'),"amount":amount,"narration":f"You have withdrawn Ksh {amount} on {date} "}
            self.withdrawals.append(withdraws_detail)
            return f"Hello,{self.account_name}{self.withdrawals}"

     def deposits_statement(self):
        for y in self.deposit:
            print (y)

     def withdrawals_statement(self):
        for x in self.withdraw:
            print (x)

     def current_balance(self):
        balance=self.balance
        return f"Your current balance is Ksh {balance}"

     def full_statement(self):
        statement=self.deposits+self.withdrawals
        for x in statement:
            print(x["narration"])
     def borrow(self,amount):
        dep_sum=0
        for d in self.deposits:
            dep_sum+=d["amount"]
        if amount<=0:
            return "invalid amount"
        if len(self.deposits)<10:
            return f"You can't borrow money because of few deposits made, make {10-len(self.deposits)} more deposits to qualify"
        if amount<100:
            return "You can only borrow atleast 100"
        if self.balance!=0:
            return f"You have Ksh {self.balance} in your balance so can't borrow when you have money"
        if amount> dep_sum/3:
            return f"You are not qualified to borrow this amount. You can borrow atmost {dep_sum/3}"
        if self.loan_balance!=0:
            return f"YOu have an outstanding loan of {self.loan_balance}, for you to borrow first clear "
        else:
            interest=(3/100)*amount
            self.loan_balance+=amount+interest
            return f"You have borrowed {amount} and your loan balance to be paid is equal to {self.loan}"
     def loan_repayment(self,amount):
        if amount<=0:
            return "invalid amount"
        if amount>self.loan_balance:
            request=amount-self.loan_balance
            self.loan_balance=0
            return f"Your loan balance is {self.loan_balance} { self.deposit(request)}"
        else:
            self.loan_balance=amount
            return f"You have paid a loan of Ksh {amount} and your current loan balance is {self.loan_balance} "
     def transfer(self,amount,new_account):
        if amount<=0:
            return "invalid amount"
        if amount>=self.balance:
            return "insufficient amount"
        if isinstance(new_account,Account):
            self.balance-=amount
            new_account.balance+=amount
            return f"You have transfered Ksh {amount}to {new_account} account with the name of {new_account.account_name}. Your new balance is {self.balance}"


        







