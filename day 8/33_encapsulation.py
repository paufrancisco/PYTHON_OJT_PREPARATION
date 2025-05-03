class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
        
    def deposit(self, amount):
        self.__balance += amount
        
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Not enough balance")
            
    def get_balance(self):
        return self.__balance
    
    
account = BankAccount(1000)

print(f"Old Balance: {account.get_balance()}")
account.deposit(4000)
account.withdraw(4000)
account.withdraw(4000)
account.withdraw(200)
print(f"New Balance: {account.get_balance()}")
