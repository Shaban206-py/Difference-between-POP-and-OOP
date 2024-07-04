#Predual Oriented Programing


# Initialize a bank account using a list

account = ['123456789', 'Shaban Saleem', 1000]

# Functions to manage the bank account
def deposit(account, amount):
    account[2] += amount
    print(f"Deposited {amount}. New balance is {account[2]}")

def withdraw(account, amount):
    if amount <= account[2]:
        account[2] -= amount
        print(f"Withdrew {amount}. New balance is {account[2]}")
    else:
        print("Insufficient funds")

def display_account(account):
    print(f"Account Number: {account[0]}")
    print(f"Owner: {account[1]}")
    print(f"Balance: {account[2]}")

# Example usage
print("Before transactions:")
display_account(account)

deposit(account, 500)
withdraw(account, 200)

print("\nAfter transactions:")
display_account(account)
