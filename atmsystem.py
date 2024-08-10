""" first we are defining the work of each option 
making a class of Atm and  functions of different works 
First time the balance is 0 and pin is 1234


"""


class ATM:
    def __init__(self, balance=0, pin="1234"):
        self.balance = balance
        self.pin = pin
        self.transaction_history = []

    def check_pin(self):
        attempts = 3
        while attempts > 0:
            entered_pin = input("Enter your PIN: ")
            if entered_pin == self.pin:
                return True
            else:
                attempts -= 1
                print(f"Incorrect PIN. You have {attempts} attempts left.")
        print("Too many incorrect attempts. Exiting.")
        return False

    def account_balance(self):
        print(f"Your current balance is: ${self.balance}")
        self.transaction_history.append(f"Checked balance: ${self.balance}")

    def cash_withdrawal(self):
        amount = float(input("Enter amount to withdraw: $"))
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"${amount} withdrawn. New balance: ${self.balance}")
            self.transaction_history.append(f"Withdrew: ${amount}")

    def cash_deposit(self):
        amount = float(input("Enter amount to deposit: $"))
        self.balance += amount
        print(f"${amount} deposited. New balance: ${self.balance}")
        self.transaction_history.append(f"Deposited: ${amount}")

    def change_pin(self):
        new_pin = input("Enter new PIN: ")
        confirm_pin = input("Confirm new PIN: ")
        if new_pin == confirm_pin:
            self.pin = new_pin
            print("PIN successfully changed.")
            self.transaction_history.append("Changed PIN")
        else:
            print("PINs do not match. Try again.")

    def show_transaction_history(self):
        if not self.transaction_history:
            print("No transactions yet.")
        else:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)

    def run(self):
        if not self.check_pin():
            return

        while True:
            print("\nATM Menu:")
            print("1. Account Balance")
            print("2. Cash Withdrawal")
            print("3. Cash Deposit")
            print("4. Change PIN")
            print("5. Transaction History")
            print("6. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.account_balance()
            elif choice == "2":
                self.cash_withdrawal()
            elif choice == "3":
                self.cash_deposit()
            elif choice == "4":
                self.change_pin()
            elif choice == "5":
                self.show_transaction_history()
            elif choice == "6":
                print("Exiting. Thank you for using the ATM.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    atm = ATM(balance=1000)  # Initial balance set to $1000
    atm.run()
