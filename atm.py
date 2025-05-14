class ATM:
    def __init__(self):
        self.balance = 5000
        self.pin = 1234

    def check_pin(self, input_pin):
        return input_pin == self.pin

    def check_balance(self):
        print(f"Your current balance is: {self.balance}")

    def deposit(self, input_pin, amount):
        if not self.check_pin(input_pin):
            print("Invalid PIN. Transaction cancelled.")
            return
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"₹{amount} deposited successfully.")
        self.check_balance()

    def withdraw(self, input_pin, amount):
        if not self.check_pin(input_pin):
            print("Invalid PIN. Transaction cancelled.")
            return
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient balance.")
            return
        self.balance -= amount
        print(f"₹{amount} withdrawn successfully.")
        self.check_balance()

    def exit(self):
        print("Thank you for using the ATM. Goodbye!")
        quit()



def run_atm():
    atm = ATM()

    while True:
        print("\n----- ATM Menu -----")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        try:
            choice = int(input("Choose an option (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            atm.check_balance()

        elif choice == 2:
            try:
                pin = int(input("Enter your PIN: "))
                amount = float(input("Enter amount to deposit: "))
                atm.deposit(pin, amount)
            except ValueError:
                print("Invalid input. Please enter numeric values.")

        elif choice == 3:
            try:
                pin = int(input("Enter your PIN: "))
                amount = float(input("Enter amount to withdraw: "))
                atm.withdraw(pin, amount)
            except ValueError:
                print("Invalid input. Please enter numeric values.")

        elif choice == 4:
            atm.exit()

        else:
            print("Invalid option. Please choose a number between 1 and 4.")

