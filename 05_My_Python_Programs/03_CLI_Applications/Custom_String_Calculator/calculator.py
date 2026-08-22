"""
Custom String Parser Calculator

A terminal-based calculator that parses mathematical expressions manually 
using string manipulation methods (split, pop, remove) and applies 
calculations using functools.reduce, without relying on built-in eval().

Created By: Lokendra Kushwaha
"""

from functools import reduce

def sum_number():
    """
    Parses a string of numbers separated by '+' and calculates their sum.

    Handles edge cases such as leading or trailing '+' operators (e.g., '+5+5+').
    Catches non-numeric user inputs to prevent program crashes.

    Returns:
        None: Prints the calculated sum directly to the console.
    """
    try:
        numbers = input('Enter Numbers For Addition (e.g., 9+9+9): ')
        num_list = numbers.split('+') 
        
        # Filtering edge cases like +9+9+ or 9+9+
        if num_list[0] == '' and num_list[-1] == '': 
            num_list.pop()
            num_list.remove('')
        elif num_list[0] == '': 
            num_list.remove('')
        elif num_list[-1] == '': 
            num_list.pop()

        int_list = [] 
        for str_num in num_list: 
            int_list.append(int(str_num))

        if not int_list:
            return

        total_sum = reduce(lambda x, y: x + y, int_list)
        print(f"Addition Result ➔  {total_sum}")

    except ValueError:
        print("ValueError ❌: Please enter valid integers, not alphabets or special characters.")

def sub_number():
    """
    Parses a string of numbers separated by '-' and calculates their difference.

    Handles leading and trailing '-' operators. If a leading '-' is found, 
    it correctly assigns the negative value to the first integer.

    Returns:
        None: Prints the calculated difference directly.
    """
    try:
        numbers = input('Enter Numbers For Subtraction (e.g., 9-5-2): ')
        num_list = numbers.split('-') 
        
        # Filtering edge cases like -9-9-
        if num_list[0] == '' and num_list[-1] == '': 
            num_list.pop()
            num_list.remove('')
            num_list[0] = f"-{num_list[0]}" # Manually attaching negative sign
        elif num_list[0] == '': 
            num_list.remove('')
            num_list[0] = f"-{num_list[0]}"
        elif num_list[-1] == '': 
            num_list.pop()

        int_list = [] 
        for str_num in num_list: 
            int_list.append(int(str_num))

        if not int_list:
            return

        total_sub = reduce(lambda x, y: x - y, int_list)
        print(f"Subtraction Result ➔  {total_sub}")

    except ValueError:
        print("ValueError ❌: Please enter valid integers, not alphabets or special characters.")

def mul_number():
    """
    Parses a string of numbers separated by '*' and calculates their product.

    Returns:
        None: Prints the calculated multiplication directly.
    """
    try:
        numbers = input('Enter Numbers For Multiplication (e.g., 9*9*9): ')
        num_list = numbers.split('*') 
        
        if num_list[0] == '' and num_list[-1] == '': 
            num_list.pop()
            num_list.remove('')
        elif num_list[0] == '': 
            num_list.remove('')
        elif num_list[-1] == '': 
            num_list.pop()

        int_list = [] 
        for str_num in num_list: 
            int_list.append(int(str_num))

        if not int_list:
            return

        total_mul = reduce(lambda x, y: x * y, int_list) 
        print(f"Multiplication Result ➔  {total_mul}")

    except ValueError:
        print("ValueError ❌: Please enter valid integers.")

def div_number():
    """
    Parses a string of numbers separated by '/' and calculates their division.

    Includes exception handling for zero division errors.

    Returns:
        None: Prints the calculated division directly.
    """
    try:
        numbers = input('Enter Numbers For Division (e.g., 100/5/2): ')
        num_list = numbers.split('/') 
        
        if num_list[0] == '' and num_list[-1] == '': 
            num_list.pop()
            num_list.remove('')
        elif num_list[0] == '': 
            num_list.remove('')
        elif num_list[-1] == '': 
            num_list.pop()
            
        int_list = [] 
        for str_num in num_list: 
            int_list.append(int(str_num))

        if not int_list:
            return

        total_div = reduce(lambda x, y: x / y, int_list) 
        print(f"Division Result ➔  {total_div}")

    except ValueError:
        print("ValueError ❌: Please enter valid integers.")
    except ZeroDivisionError:
        print("ZeroDivisionError ❌: Math Error! Cannot divide a number by zero.")

def main():
    """
    The main driver loop that runs the calculator application.
    Continuously prompts the user for operations until 'Exit' is passed.
    """
    while True: 
        user_input = input("\n"
                           "Enter '+' For Addition\n"
                           "Enter '-' For Subtraction\n"
                           "Enter '*' For Multiplication\n"
                           "Enter '/' For Division\n"
                           "Enter 'Exit' to Quit\n"
                           "--------> ").strip().lower() 
        
        if user_input == 'exit':
            print("Exiting Calculator. Have a great day!")
            break
        elif user_input == '+':
            sum_number()
        elif user_input == '-':
            sub_number()
        elif user_input == '*':
            mul_number()
        elif user_input == '/':
            div_number()
        else:
            print("Invalid Input! Please select a valid operator.")

if __name__ == "__main__":
    main()