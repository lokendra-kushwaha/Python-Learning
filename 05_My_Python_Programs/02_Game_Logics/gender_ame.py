import requests
import time

def predict_gender():
    print("🤖 Welcome to the Advanced AI Gender Predictor!")
    print("-" * 45)
    
    # Starting the infinite loop
    while True:
        # Take input from the user
        original_name = input("\nPlease enter a name (or type 'exit' to quit): ").strip()
        
        # Condition to stop the program if user types 'exit'
        if original_name.lower() == 'exit':
            print("\nShutting down the system... Goodbye! 👋")
            break # This breaks the loop and stops the program
            
        # If the user just presses enter without typing a name
        if original_name == "":
            print("Please type a valid name!")
            continue
            
        # Convert the name to lowercase for checking
        name_for_checking = original_name.lower()
        
        # Prank condition for friend and VIP condition for you
        target_friend = "vivek" 
        my_name = "lokendra"
        
        # Suspense building / Fake hacking effects
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
        
        # 1. Prank Condition: Check if "vivek" is in the input
        if target_friend in name_for_checking:
            print(f"🎯 Prediction: {original_name}, you are 100% GAY! 🏳️‍🌈🤣")
            
        # 2. VIP Condition: Check if "lokendra" is in the input
        elif my_name in name_for_checking:
            print(f"🎯 Prediction: {original_name.capitalize()} is Male (Accuracy: 100.0%) 😎")
            
        # 3. Normal Condition: Fetch real prediction from the API for everyone else
        else:
            first_name = name_for_checking.split()[0]
            
            try:
                url = f"https://api.genderize.io/?name={first_name}"
                response = requests.get(url).json()
                
                # If the API successfully finds a gender
                if response.get('gender') is not None:
                    real_gender = response['gender'].capitalize()
                    accuracy = response['probability'] * 100
                    print(f"🎯 Prediction: {original_name.capitalize()} is {real_gender} (Accuracy: {accuracy}%)")
                else:
                    print("😅 Sorry, this name was not found in our database. Please try a common name!")
                    
            except Exception as e:
                print("⚠️ An error occurred. Please check your internet connection.")
                
        # Printing a line to separate results for the next name
        print("-" * 45)

# Run the program
if __name__ == "__main__":
    predict_gender()