"""
Prime Factorization in a Range 🧮

A mathematical script that calculates and prints the prime factors 
for every number within a user-defined range. Demonstrates nested 
loops (for and while) and modulo arithmetic.

Created By: Lokendra Kushwaha
"""

def main():
    print("=" * 50)
    print("         🧮 PRIME FACTORIZATION FINDER 🧮         ")
    print("=" * 50)

    start_num = int(input("Enter Your Starting Number: "))
    end_num = int(input("Enter Your Ending Number: "))
    
    print("-" * 50)
    
    # Loop through the given range
    for number in range(start_num, end_num + 1):
        print(f"Prime factors of {number} ➔ ", end="")
        
        i = 2
        temp_num = number  # Using a temporary variable to perform division
        
        while temp_num > 1:
            if temp_num % i == 0:
                print(i, end=" ")
                temp_num = temp_num // i
            else:
                i += 1
                
        print()  # For a new line after each number's factors

    print("=" * 50)

if __name__ == "__main__":
    main()