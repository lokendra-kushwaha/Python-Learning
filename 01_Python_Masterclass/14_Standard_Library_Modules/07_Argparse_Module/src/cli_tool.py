"""
====================================================================================
🛠️ STANDARD LIBRARY: THE 'argparse' MODULE
====================================================================================
Description: 'argparse' is the recommended built-in module for writing 
             Command Line Interfaces (CLI). It parses arguments directly from 
             the terminal and automatically generates help and usage messages.
====================================================================================
"""

import argparse
import sys

def main():
    # 1. Initialize the Parser (This is the architect of your CLI)
    parser = argparse.ArgumentParser(
        description="🚀 Lokendra's Super CLI Tool: A script to greet users and perform basic math."
    )

    # 2. Add Arguments (What inputs do we expect from the terminal?)
    
    # REQUIRED Argument (Positional)
    parser.add_argument(
        "name", 
        type=str, 
        help="The name of the user you want to greet."
    )

    # OPTIONAL Argument (Flag with double dashes '--')
    parser.add_argument(
        "--age", 
        type=int, 
        default=18, 
        help="Age of the user (Optional, defaults to 18)."
    )

    # TRUE/FALSE Flag (Action='store_true' means if user types --vip, it becomes True)
    parser.add_argument(
        "--vip", 
        action="store_true", 
        help="Mark the user as a VIP guest!"
    )

    # 3. Parse the Arguments (Read what the user typed in the terminal)
    args = parser.parse_args()

    # 4. Use the Arguments in our Logic
    print("\n" + "=" * 50)
    
    if args.vip:
        print(f"🌟 WELCOME VIP GUEST: {args.name.upper()} 🌟")
    else:
        print(f"👋 Hello there, {args.name}!")
        
    print(f"🎂 Age recorded as: {args.age}")
    print("=" * 50 + "\n")

# This ensures the script only runs when executed directly from the terminal
if __name__ == "__main__":
    main()