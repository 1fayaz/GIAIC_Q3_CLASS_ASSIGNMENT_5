# **ATM Simulation using Object-Oriented Programming (OOP)**

## **Overview**

This project is an **ATM (Automated Teller Machine) Simulation** implemented in Python, demonstrating the use of **Object-Oriented Programming (OOP)** principles. The program allows the user to interact with a simulated ATM to perform basic banking operations, such as checking account balance, depositing money, withdrawing money, and exiting the program. The primary focus of this project is to showcase the use of **class-based structures** and **encapsulate functionality** within methods that handle various banking actions.

## **Class Overview**

The `ATM` class models the behavior of an ATM machine, with the following attributes and methods:

### **Attributes:**
- **balance**: The initial balance of the ATM account, set to **5000 rupees**.
- **pin**: The default PIN for the ATM, set to **1234**.

### **Methods:**
1. **check_pin(input_pin)**: Verifies if the entered PIN matches the stored PIN.
2. **check_balance()**: Displays the current account balance.
3. **deposit(amount)**: Allows the user to deposit money into the account (requires valid PIN).
4. **withdraw(amount)**: Allows the user to withdraw money from the account (requires valid PIN and sufficient balance).
5. **exit()**: Terminates the program.

## **Features**
- **PIN Validation**: The program requires a valid PIN before allowing deposit or withdrawal transactions.
- **Transaction Rules**:
  - Prevents **negative deposit amounts**.
  - Prevents **withdrawals that exceed the available balance**.
  - **Gracefully handles invalid user inputs** (e.g., non-numeric inputs).
- **User Interface**: A simple menu-driven interface allows users to interact with the ATM and choose different operations.

## **Requirements**
- Python 3.x

## **How to Run**
1. Clone or download the repository to your local machine.
2. Open a terminal or command prompt and navigate to the folder where the project is located.
3. Run the Python file using the command:
   ```bash
   python atm.py
