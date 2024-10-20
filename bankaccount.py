from datetime import datetime
import getpass

class BankAccount:
    def __init__(self, account_number, customer_name, password, balance=0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.password = password
        self.balance = balance
        self.date_of_opening = datetime.now()

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}"
        else:
            return "Invalid deposit amount"

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                return f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}"
            else:
                return "Insufficient balance"
        else:
            return "Invalid withdrawal amount"

    def check_balance(self):
        return f"Current balance: ${self.balance:.2f}"

    def customer_details(self):
        return f"Customer Name: {self.customer_name}\n" \
               f"Account Number: {self.account_number}\n" \
               f"Account Opening Date: {self.date_of_opening.strftime('%Y-%m-%d')}\n" \
               f"Current Balance: ${self.balance:.2f}"

class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, customer_name, password, initial_balance):
        if account_number not in self.accounts:
            self.accounts[account_number] = BankAccount(account_number, customer_name, password, initial_balance)
            return "Account created successfully"
        return "Account number already exists"

    def login(self, account_number, password):
        if account_number in self.accounts and self.accounts[account_number].password == password:
            return self.accounts[account_number]
        return None

def main():
    bank = BankSystem()

    while True:
        print("\nWelcome to the Bank Account Management System")
        print("1. Login")
        print("2. Sign Up")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            account_number = input("Enter account number: ")
            password = getpass.getpass("Enter password: ")
            account = bank.login(account_number, password)
            if account:
                print("Login successful!")
                handle_account_operations(account)
            else:
                print("Invalid account number or password")
        elif choice == '2':
            account_number = input("Enter new account number: ")
            customer_name = input("Enter customer name: ")
            password = getpass.getpass("Enter password: ")
            initial_balance = float(input("Enter initial balance: $"))
            result = bank.create_account(account_number, customer_name, password, initial_balance)
            print(result)
        elif choice == '3':
            print("Thank you for using the Bank Account Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def handle_account_operations(account):
    while True:
        print("\nWhat would you like to do?")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. View Customer Details")
        print("5. Logout")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            amount = float(input("Enter deposit amount: $"))
            print(account.deposit(amount))
        elif choice == '2':
            amount = float(input("Enter withdrawal amount: $"))
            print(account.withdraw(amount))
        elif choice == '3':
            print(account.check_balance())
        elif choice == '4':
            print(account.customer_details())
        elif choice == '5':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()