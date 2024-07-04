# Object Oriented Programing


class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account = [account_number, owner, balance]

    def deposit(self, amount):
        self.account[2] += amount
        print(f"Deposited {amount}. New balance is {self.account[2]}")

    def withdraw(self, amount):
        if amount <= self.account[2]:
            self.account[2] -= amount
            print(f"Withdrew {amount}. New balance is {self.account[2]}")
        else:
            print("Insufficient funds")

    def display_account(self):
        print(f"Account Number: {self.account[0]}")
        print(f"Owner: {self.account[2]}")
        print(f"Balance: {self.account[2]}")

# Example usage
account1 = BankAccount('123456789', 'Shaban Saleem', 1000)

print("Before transactions:")
account1.display_account()

account1.deposit(500)
account1.withdraw(200)

print("\nAfter transactions:")
account1.display_account()
