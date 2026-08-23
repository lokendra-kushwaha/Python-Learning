"""
Number Comparison Utility
-------------------------
A simple Python program that takes two numerical inputs from the user 
and determines which number is greater, lesser, or if they are equal.

Features:
- Includes input validation to prevent crashes if a non-integer is entered.
- Uses f-strings for clean output formatting.
"""

def get_valid_integer(prompt_message: str) -> int:
    """
    Prompts the user for input and ensures it is a valid integer.
    
    Args:
        prompt_message (str): The message displayed to the user.
        
    Returns:
        int: A valid integer provided by the user.
    """
    while True:
        try:
            return int(input(prompt_message))
        except ValueError:
            # Catches the error if user types letters or symbols instead of numbers
            print("Invalid input! Please enter a valid whole number.")
            continue

def compare_numbers():
    """
    Main logic function to compare two numbers and print the results.
    """
    print("=== Number Comparator ===")
    num1 = get_valid_integer("Enter First Number : ")
    num2 = get_valid_integer("Enter Second Number : ")

    if num1 == num2:
        print("\nAnswer -: ")
        print("Both numbers are equal.")
        
    elif num1 > num2:
        print("\nAnswer -: ")
        print(f"{num1} is Greater than {num2}.") 
        print(f"{num2} is Lesser than {num1}.")
        
    else:
        print("\nAnswer -: ")
        print(f"{num2} is Greater than {num1}.")
        print(f"{num1} is Lesser than {num2}.")

# Entry point of the script
if __name__ == "__main__":
    compare_numbers()