class BankMachine:
    def __init__(self):
        self.__account_balance = 5000
        self.__account_pin = 1234

    def verify_pin(self, entered_pin: int):
        return entered_pin == self.__account_pin

    def view_balance(self, entered_pin):
        if self.verify_pin(entered_pin):
            print(f"Your current balance is: {self.__account_balance} rupees.")
        else:
            print("Incorrect PIN entered!")

    def deposit_money(self, amount, entered_pin):
        if not self.verify_pin(entered_pin):
            print("Incorrect PIN entered!")
        elif amount > 0:
            self.__account_balance += amount
            print(f"Deposited {amount} rupees.")
            print(f"Updated balance: {self.__account_balance} rupees.")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw_money(self, amount, entered_pin):
        if not self.verify_pin(entered_pin):
            print("Incorrect PIN entered!")
        elif amount > self.__account_balance:
            print("Insufficient funds in your account.")
        elif amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        else:
            self.__account_balance -= amount
            print(f"Withdrawn {amount} rupees.")
            print(f"Updated balance: {self.__account_balance} rupees.")

    def exit_machine(self):
        print("Shutting down ATM simulation.")