"""
=========================================================
💎 CUSTOM DIAMOND PATTERN PRINTER 💎
=========================================================

Description:
    A classic pattern printing program that generates a symmetric 
    diamond shape based on a user-provided odd number. 
    It leverages Python's string multiplication feature to avoid 
    deeply nested loops, making the code highly efficient and clean.

Created By: Lokendra Kushwaha
"""

def main():
    print("=" * 50)
    print("           💎 DIAMOND PATTERN MAKER 💎           ")
    print("=" * 50)

    # Taking an odd number from the user
    try:
        n = int(input("\nEnter an Odd Number (e.g., 5, 7, 9): "))
        
        if n % 2 == 0:
            print("⚠️ Please enter an ODD number for a perfect diamond!")
            return
            
    except ValueError:
        print("❌ Invalid input! Please enter a valid integer.")
        return

    print(f"\nHere is your {n}x{n} diamond:\n")

    # ==========================================
    # FOR UPPER PART (Including Middle Row)
    # ==========================================
    for i in range(1, n + 1, 2):  # Start: 1, End: n, Step: 2
        spaces = (n - i) // 2     # Calculating Spaces using floor division
        print(" " * spaces + "*" * i)

    # ==========================================
    # FOR LOWER PART
    # ==========================================
    for i in range(n - 2, 0, -2): # Start: n-2, End: 1, Step: -2
        spaces = (n - i) // 2     # Calculating Spaces
        print(" " * spaces + "*" * i)
        
    print("\n" + "=" * 50)

if __name__ == "__main__":
    main()