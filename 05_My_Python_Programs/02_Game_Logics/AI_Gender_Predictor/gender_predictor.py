"""
Advanced AI Gender Predictor Tool.

This module provides a terminal-based application that predicts a person's gender 
based on their first name using the external Genderize.io API. 
It also contains hidden custom "easter eggs" (prank logic) for specific users.

Example:
    Run the script directly from the terminal:
        $ python gender_predictor.py
"""

import requests
import time

def predict_gender():
    """
    Runs the interactive gender prediction application.

    This function continuously prompts the user for a name, simulates a 
    complex "hacking/scanning" process for suspense, and then outputs a 
    gender prediction. It handles specific target names internally for 
    humorous purposes, while processing all other names through a live API.

    Features:
        - Interactive continuous loop until 'exit' is invoked.
        - Artificial delay to simulate heavy data processing.
        - Custom hardcoded responses (Easter Eggs) for specific names.
        - External API integration (api.genderize.io) for real predictions.
        - Exception handling for missing inputs and network failures.
    """
    print("🤖 Welcome to the Advanced AI Gender Predictor!")
    print("-" * 45)
    
    # Start the continuous execution loop
    while True:
        # Prompt the user for a name input and remove leading/trailing spaces
        original_name = input("\nPlease enter a name (or type 'exit' to quit): ").strip()
        
        # Termination condition: break the loop if the user types 'exit'
        if original_name.lower() == 'exit':
            print("\nShutting down the system... Goodbye! 👋")
            break 
            
        # Input validation: check for empty inputs
        if original_name == "":
            print("[!] Please type a valid name!")
            continue
            
        # Convert input to lowercase for case-insensitive condition checking
        name_for_checking = original_name.lower()
        
        # Define target names for custom responses
        target_friend = "vivek" 
        my_name = "lokendra"
        
        # Simulate a deep system analysis process with artificial delays
        print("\n[+] Connecting to Global Database...")
        time.sleep(2)
        print("[+] Bypassing security protocols...")
        time.sleep(2)
        print("[+] Running Deep Neural Network scan...")
        time.sleep(2)
        print("[+] Analyzing digital footprint and behavioral data...")
        time.sleep(2)
        
        print("\n✅ Analysis Complete! Generating Results...\n")
        time.sleep(1)
        
        # Condition 1: Easter Egg / Prank condition for the specific friend
        if target_friend in name_for_checking:
            print(f"🎯 Prediction: {original_name}, you are 100% GAY! 🏳️‍🌈🤣")
            
        # Condition 2: VIP condition for the developer
        elif my_name in name_for_checking:
            print(f"🎯 Prediction: {original_name.capitalize()} is Male (Accuracy: 100.0%) 😎")
            
        # Condition 3: Default logic fetching actual data via API
        else:
            # Extract the first name to ensure accurate API results
            first_name = name_for_checking.split()[0]
            
            try:
                # Construct the API endpoint URL and fetch the JSON response
                url = f"https://api.genderize.io/?name={first_name}"
                response = requests.get(url).json()
                
                # Verify if the API successfully returned a gender prediction
                if response.get('gender') is not None:
                    real_gender = response['gender'].capitalize()
                    accuracy = response['probability'] * 100
                    print(f"🎯 Prediction: {original_name.capitalize()} is {real_gender} (Accuracy: {accuracy}%)")

                else:
                    print("😅  Sorry, this name was not found in our database. Please try a common name!")
                    
            except Exception as e:
                # Handle potential network errors or API failures gracefully
                print("⚠️  An error occurred. Please check your internet connection.")
                
        # Visual separator for the next iteration
        print("-" * 45)


# ==========================================
#              MAIN EXECUTION
# ==========================================

if __name__ == "__main__":
    predict_gender()