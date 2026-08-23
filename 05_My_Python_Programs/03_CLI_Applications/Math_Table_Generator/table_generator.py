"""
Multiplication Table Generator 🔢

A CLI utility that generates a complete multiplication table for any 
given number. It also allows the user to query a specific multiple 
using structural pattern matching.

Created By: Lokendra Kushwaha
"""

def main():
    print("=" * 50)
    print("       🔢 MULTIPLICATION TABLE GENERATOR 🔢       ")
    print("=" * 50)

    while True:
        num = int(input("\nEnter a Number to create Table (or '0' to Exit): "))
        if num == 0:
            print("Keep practicing your math! Goodbye. 👋")
            break
        
        print("-" * 30)
        # Generating the table
        for i in range(1, 11):
            print(f"{num} X {i} = {num * i}")
        print("-" * 30)

        # Asking for a specific multiple
        x = int(input(f"Want to print a specific multiple of {num}? (Enter 1-10, or '0' to exit): "))

        if x == 0:
            print("Keep practicing your math! Goodbye. 👋")
            break

        print("-" * 30)
        if 1 <= x <= 10:

            match x:
                case 1:
                    print(f"➔ The 1st multiple of {num} is {num * x}")
                case 2:
                    print(f"➔ The 2nd multiple of {num} is {num * x}")
                case 3:
                    print(f"➔ The 3rd multiple of {num} is {num * x}")
                case 4 | 5 | 6 | 7 | 8 | 9 | 10:
                    # Grouped the rest since they all end in 'th'
                    print(f"➔ The {x}th multiple of {num} is {num * x}")
        else:
            print("❌ Invalid Input! Please enter a number between 1 and 10.")
        print("-" * 30)

if __name__ == "__main__":
    main()