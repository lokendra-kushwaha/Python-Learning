"""
Ultimate AI Love Calculator (Prank Edition).

This module combines a Love Calculator with the Genderize.io API to predict 
the gender of the entered names. If it detects two males or two females, 
it throws a hilarious custom prank message instead of a percentage.

Example:
    Run the script directly from the terminal:
        $ python ultimate_love_calculator.py
"""

import random
import time
import requests

def get_gender(name):
    """
    Fetches the gender of a given name using the Genderize.io API.

    This is a helper function. It runs quietly in the background without 
    artificial delays or print statements, making it extremely fast.

    Args:
        name (str): The first name of the person.

    Returns:
        str: The predicted gender ('Male', 'Female') or 'Unknown' if not found/error.
    """
    first_name = name.strip().split()[0].lower()
    try:
        url = f"https://api.genderize.io/?name={first_name}"
        response = requests.get(url, timeout=5).json()
        
        if response.get('gender') is not None:
            return response['gender'].capitalize()
    except Exception:
        # If internet is down or API fails, return Unknown so the game doesn't crash
        pass
    
    return "Unknown"


def run_ultimate_calculator():
    """Executes the Ultimate Love Calculator application."""
    print("-" * 60)
    print("💖 Welcome to the AI-Powered Love Calculator! 💖")
    print("-" * 60 + "\n")

    your_name = input("Enter Your Name: ").strip().title()
    partner_name = input("Enter Your Partner's Name: ").strip().title()
    
    while True:
        user_input = input("\nType '1' or 'Calculate' to see the magic: ").strip().title()
        
        if user_input in ["1", "Calculate"]:
            print("\n[+] Scanning digital compatibility... ✨")
            
            # Background API Calls (Fast, no fake sleep here)
            gender1 = get_gender(your_name)
            gender2 = get_gender(partner_name)
            
            time.sleep(1) 
            print("\n✅ Analysis Complete!\n")
            
            # The Master Prank Logic (Fully in English now)
            if gender1 == "Male" and gender2 == "Male":
                print(f"🚨 ALERT! {your_name} and {partner_name} are both MALES!")
                print("🏳️‍🌈 Result: 100% GAY! The bromance is off the charts! What are you two hiding? 🤣")
                
            elif gender1 == "Female" and gender2 == "Female":
                print(f"🚨 ALERT! {your_name} and {partner_name} are both FEMALES!")
                print("👯‍♀️ Result: 100% LESBIAN! 'Just besties', right? We see exactly what's going on here! 🤣")
                
            else:
                # Normal Love Calculator Logic (If Male + Female, or Unknown)
                love_percentage = random.randint(1, 100)
                print(f"💘 Love Percentage between {your_name} & {partner_name} is:")
                
                if love_percentage >= 80:
                    print(f"🔥 {love_percentage}% - A match made in heaven! 💍")
                elif love_percentage >= 50:
                    print(f"😊 {love_percentage}% - Good chances! Keep putting in the effort. 💐")
                else:
                    print(f"😅 {love_percentage}% - Yikes! You might want to just stay friends. 🏃‍♂️")
            
            print("\n" + "-" * 60)
            break
            
        else:
            print("[!] Invalid Input! Please type '1' or 'Calculate'.")


# ==========================================
#              MAIN EXECUTION
# ==========================================
if __name__ == "__main__":
    run_ultimate_calculator()