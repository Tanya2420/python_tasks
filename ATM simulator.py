
# ATM class to simulate ATM functionality
class ATM:
    def __init__(self, balance=10000):
        self.balance = balance

    def check_balance(self):
        return f"Your balance is ${self.balance}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"${amount} deposited. Your new balance is ${self.balance}"
        else:
            return "Invalid amount. Please enter a positive value."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"${amount} withdrawn. Your new balance is ${self.balance}"
        elif amount > self.balance:
            return "Insufficient funds. Your balance is not enough for this withdrawal."
        else:
            return "Invalid amount. Please enter a positive value."

# Main program loop
def main():
    atm = ATM()

    while True:
        print("\nATM Simulator")
        print("1. Check Balance")
        print("2. Deposit Funds")
        print("3. Withdraw Funds")
        print("4. Exit")

        choice = input("Select an option (1/2/3/4): ")

        if choice == "1":
            print(atm.check_balance())
        elif choice == "2":
            amount = float(input("Enter the amount to deposit: $"))
            print(atm.deposit(amount))
        elif choice == "3":
            amount = float(input("Enter the amount to withdraw: $"))
            print(atm.withdraw(amount))
        elif choice == "4":
            print("Thank you for using the ATM. Have a great day!")
            break
        else:
            print("Invalid choice. Please select a valid option (1/2/3/4).")

if __name__ == "__main__":
    main()
