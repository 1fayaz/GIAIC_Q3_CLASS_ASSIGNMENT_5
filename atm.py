from file_utils import BankMachine

atm_system = BankMachine()

while True:
    print("\n--- ATM Simulation ---")
    print("1. View Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    user_choice = int(input("Select an option: "))
 
    if user_choice == 1:
        pin = int(input("Enter PIN to view balance: "))
        atm_system.view_balance(pin)

    elif user_choice == 2:
        pin = int(input("Enter PIN to deposit money: "))
        amount = int(input("Enter the deposit amount: "))
        atm_system.deposit_money(amount, pin)

    elif user_choice == 3:
        pin = int(input("Enter PIN to withdraw money: "))
        amount = int(input("Enter the withdrawal amount: "))
        atm_system.withdraw_money(amount, pin)

    elif user_choice == 4:
        atm_system.exit_machine()
        break

    else:
        print("Invalid option. Please try again.")

print("\nThank you for using the ATM Simulation!")
