"""
=========================================================
🏦 BASIC ATM / BANK SIMULATION 🏦
=========================================================

Description:
    A classic beginner program to simulate an ATM machine.
    Demonstrates the use of infinite while-loops, user input handling, 
    and basic state management (keeping track of account balance).

Created By: Lokendra Kushwaha
"""

def main():
    print("=" * 40)
    print("      🏦 WELCOME TO PYTHON BANK 🏦      ")
    print("=" * 40)

    balance = 10000  

    while True:
        print("\n--- Main Menu ---")
        print("1. Balance Check")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Exit")
        
        try:
            user_input = int(input("\nEnter Your Choice (1-4): "))
        except ValueError:
            print("❌ Invalid input! Please enter a number.")
            continue

        if user_input == 1:
            pin = input("Enter Your PIN for Balance Check: ")
            print(f"💰 Your Current Balance is: {balance} Rs.")

        elif user_input == 2:
            withdraw = int(input("Enter Amount to Withdraw: Rs. "))
            if withdraw <= balance:
                balance -= withdraw 
                print(f"✅ Transaction Successful! Your new balance is: {balance} Rs.")
            else:
                print("❌ Insufficient Funds!")

        elif user_input == 3:
            deposit = int(input("Enter Amount to Deposit: Rs. "))
            balance += deposit 
            print(f"✅ Transaction Successful! Your new balance is: {balance} Rs.")

        elif user_input == 4:
            print("🙏 Thank You for using Python Bank. Have a great day!")
            break

        else:
            print("⚠️ Invalid Choice! Please select an option from 1 to 4.")

if __name__ == "__main__":
    main()