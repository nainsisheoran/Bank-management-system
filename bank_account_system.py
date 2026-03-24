#design a bank account system using oops concept where:
#the base class bankaccount has attributes account number, balance,and methods deposits () and withdraw()
#the derived class saving accounts has an additional interest rate attribute and a method apply_interest calculate interest and update the balance

class bankAccount:
     def __init__(self,acc_number,balance):
          self.acc_number=acc_number
          self.balance=balance
     def deposit(self,amount):
          #self.deposit_amt=amount
          self.balance+=amount
          print("amount deposited: ",amount)
          print("Updated balance: ",self.balance)
     """def update_amt(self,amount):
          self.update_amt=amount
          updated_amt= self.balance+self.amount                                      
     print("Updated Balance : ",amount)    """

     def withdraw(self,amount):
          #self.withdraw_amt=withdraw_amt
          if amount > self.balance:
               print("Insufficient balance.")
          else:
               self.balance -= amount  
               print("amount withdrawn:", amount)
               print("remaining balance:", self.balance)   

class savingAccount(bankAccount):
     def __init__(self, acc_number, balance,interest_rate):
          super().__init__(acc_number, balance)    
          self.interest_rate=interest_rate 

     def apply_interest(self):
          interest=self.balance * self.interest_rate / 100
          self.balance +=interest
          print("interest added:", interest)
          print("balance after interest: ",self.balance)

     """def calculate_interest(self,cal_interest):
          return self.balance*self.interest_rate
     def update_balance(self,update_bal):     """
acc_no=input("Enter account number: ")
balance=float(input("Enter initial balance:"))
interest_rate=float(input("Enter interest rate (%):"))

account=savingAccount(acc_no, balance, interest_rate)

deposit_amt=float(input("Enter ammount to deposit: "))
account.deposit(deposit_amt)

withdraw_amount=float(input("enter ammount to withdraw:"))
account.withdraw(withdraw_amount)
account.apply_interest()

print("Final balance:", account.balance)