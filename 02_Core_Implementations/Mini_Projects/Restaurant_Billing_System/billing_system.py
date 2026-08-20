"""
Restaurant Billing System

A command-line application that takes customer orders, calculates the total bill 
using a predefined menu dictionary, and applies dynamic discounts based on the total amount.
"""

def calculate_discount(total_bill):
    """
    Calculates the final bill amount and the applied discount percentage.
    
    Args:
        total_bill (int): The initial total amount of the order.
        
    Returns:
        tuple: A tuple containing (final_amount, discount_percentage)
    """
    if total_bill < 500:
        return total_bill, 0
    elif 500 <= total_bill < 1000:
        # 10% discount
        return total_bill * 0.90, 10
    else:
        # 20% discount
        return total_bill * 0.80, 20


def main():
    """Main function to run the Restaurant Billing System."""
    menu = {'Tea': 20, 'Samosa': 30, 'Pizza': 499, 'Burger': 50}
    total_bill = 0
    
    print("=" * 40)
    print("Welcome to our Restaurant!")
    print("=" * 40)
    
    print("\n--- Our Menu ---")
    for item, price in menu.items():
        print(f"{item}: {price} Rs")
        
    print("\nType 'done' when your order is complete.")
    print(" Offers: Get a 10% discount on orders above 500 Rs, and 20% on orders above 1000 Rs! \n")
    
    while True:
        # Getting user input with proper title casing and removing extra spaces
        item = input("What would you like to order? (or type 'done' for the bill): ").title().strip()
        
        if item == "Done":
            print("\nYour order is complete. Calculating bill...")
            break
        elif item in menu:
            rate = menu[item]
            total_bill += rate
            print(f" -> Great! {item} added to your order. (Price: {rate} Rs)")
        else:
            print(" -> Sorry, we don't have this item. Please choose from the menu.")

    # Process and display the final bill if the user ordered something
    if total_bill > 0:
        final_amount, discount_pct = calculate_discount(total_bill)
        
        print("\n" + "=" * 40)
        if discount_pct == 0:
            print(f"Your total bill is: {final_amount} Rs.")
        else:
            print(f"Your total bill is: {final_amount} Rs. (After {discount_pct}% Discount)")
            
        print("Thank you, visit again!")
        print("=" * 40 + "\n")
    else:
        print("\nYou didn't order anything. See you next time!\n")

if __name__ == "__main__":
    main()