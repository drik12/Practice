class BankAccount:
    def __init__(self, id, balance=0):
        self.id = id
        self.balance = 0

    def deposit(self, amount):
            print("Depositing amount:", amount)
            self.balance += amount

    def withdraw(self, amount):
            print("Withdrawing amount:", amount)
            self.balance -= amount
    
    def __str__(self):
            return f"Account ID: {self.id}, Balance: {self.balance}"
    
acc1 = BankAccount(1)
acc1.deposit(500)
acc1.withdraw(200)
print(acc1)