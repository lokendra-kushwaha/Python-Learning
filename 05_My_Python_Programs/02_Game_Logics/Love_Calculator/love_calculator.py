"""
Love Calculator Prank Game.

This module provides a fun, terminal-based Love Calculator that generates 
a random romantic compatibility percentage between two individuals. 

Example:
    Run the script directly from the terminal to play:
        $ python love_calculator.py
"""

import time, random
def run_love_calculator():
    """
    Executes the Love Calculator application.

    Prompts the user for their name and their partner's name, creates artificial 
    suspense, and outputs a randomly generated love percentage along with a 
    customized romantic (or funny) message.
    """
    print("-" * 60)
    print("💖 Welcome to the Ultimate Love Calculator! 💖")
    print("        How much is he/she into you?        ")
    print("-" * 60 + "\n")

    # Prompt user for names and format them nicely with .title()
    your_name = input("Enter Your Name: ").strip().title()
    partner_name = input("Enter Your Partner's Name: ").strip().title()
    
    # Use a while loop to handle invalid inputs gracefully
    while True:
        # Prompt user to trigger the calculation
        user_input = input("\nType '1' or 'Calculate' to see the magic: ").strip().title()
        
        # Check if the user typed '1' or 'Calculate'
        if user_input in ["1", "Calculate"]:
            
            # Artificial suspense for dramatic effect
            print("\n[+] Consulting the stars... ✨")
            time.sleep(1)
            print("[+] Calculating romantic compatibility... 💘")
            time.sleep(1)
            
            # Generate a random love percentage between 1 and 100
            love_percentage = random.randint(1, 100)
            
            print(f"\n✅ Result: Love Percentage between {your_name} & {partner_name} is:")
            
            # Display custom messages based on the randomized score
            if love_percentage >= 80:
                print(f"🔥 {love_percentage}% - Made for each other! (Rab Ne Bana Di Jodi) 💍")
            elif love_percentage >= 50:
                print(f"😊 {love_percentage}% - Good chances! Keep putting in effort. 💐")
            else:
                print(f"😅 {love_percentage}% - Yikes! You might want to just stay friends. 🏃‍♂️")
            
            print("\n" + "-" * 60)
            break # Exit the loop after successful calculation
            
        else:
            # Handle invalid input and prompt again
            print("[!] Invalid Input! Please type '1' or 'Calculate'.")


# ==========================================
#              MAIN EXECUTION
# ==========================================
if __name__ == "__main__":
    run_love_calculator()