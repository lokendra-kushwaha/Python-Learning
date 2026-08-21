"""
Kaun Banega Crorepati (KBC) Simulation

A terminal-based trivia game inspired by KBC.
Features dynamic prize mapping, safe havens (milestones), and early quit options.

Created By: Lokendra Kushwaha
"""

def play_kbc():
    print("🎉 Welcome to Kaun Banega Crorepati (KBC) 🎉")
    print("Rules:")
    print("1. There are 10 questions. Answer them to win up to ₹7,00,00,000!")
    print("2. Safe havens (Milestones) are at Question 4 (₹10,000) and Question 8 (₹2,00,00,000).")
    print("3. Type 'Q' anytime to Quit and take your current winnings home.\n")
    print("=" * 70)

    # Core Data Structure: [Question, Opt A, Opt B, Opt C, Opt D, Correct_Option]
    kbc_data = [
        ["What is the capital of India?", "Mumbai", "New Delhi", "Kolkata", "Chennai", "B"],
        ["According to the Ramayana, what was the name of Lord Rama's father?", "Janaka", "Ravana", "Dasharatha", "Valmiki", "C"],
        ["Which is the largest planet in our solar system?", "Earth", "Mars", "Saturn", "Jupiter", "D"],
        ["How many days are there in a week?", "5", "6", "7", "8", "C"],
        ["Which is the highest mountain peak in the world?", "Kangchenjunga", "Mount Everest", "K2", "Makalu", "B"],
        ["Who was the first Prime Minister of India?", "Lal Bahadur Shastri", "Indira Gandhi", "Jawaharlal Nehru", "Mahatma Gandhi", "C"],
        ["How many bones are there in a normal adult human body?", "200", "206", "208", "210", "B"],
        ["In which city is the 'Gateway of India' located?", "Delhi", "Mumbai", "Agra", "Jaipur", "B"],
        ["Who invented the telephone?", "Thomas Edison", "Nikola Tesla", "Alexander Graham Bell", "Albert Einstein", "C"],
        ["Who was the first Indian to win a Nobel Prize?", "C. V. Raman", "Rabindranath Tagore", "Mother Teresa", "Amartya Sen", "B"]
    ]

    # Array mapping for prize money
    levels = [1000, 2000, 5000, 10000, 500000, 1000000, 10000000, 20000000, 50000000, 70000000]
    
    money = 0
    guaranteed_money = 0

    for i in range(len(kbc_data)):
        question = kbc_data[i]
        # Using string formatting for commas in prize money (e.g., 10,000)
        print(f"\n📺 Question {i + 1} for ₹{levels[i]:,}")
        print(f"Q: {question[0]}")
        print(f"A. {question[1]:<22} B. {question[2]}")
        print(f"C. {question[3]:<22} D. {question[4]}")

        # Input validation loop
        while True:
            reply = input("Enter your answer (A/B/C/D) or 'Q' to Quit: ").upper().strip()
            if reply in ['A', 'B', 'C', 'D', 'Q']:
                break
            print("Invalid Input! Please select A, B, C, D, or Q.")

        # Quit logic
        if reply == 'Q':
            print(f"\n🚶‍♂️ You decided to quit. You are taking home ₹{money:,}!")
            return # Exits the function completely

        # Checking the Answer
        if reply == question[5]:
            money = levels[i]
            print(f"✅ Correct Answer! You have won ₹{money:,}")
            
            # Milestone updating logic
            if i == 3:  # 4th Question
                guaranteed_money = 10000
                print("🌟 Milestone Reached! You are guaranteed at least ₹10,000.")
            elif i == 7:  # 8th Question
                guaranteed_money = 20000000
                print("🌟 Milestone Reached! You are guaranteed at least ₹2,00,00,000.")
        else:
            print(f"❌ Wrong Answer! The correct answer was {question[5]}.")
            print(f"Game Over! You are dropping down to your last safe haven.")
            money = guaranteed_money
            break # Breaks out of the loop

    print("\n" + "=" * 70)
    print(f"🏆 Your final take-home money is: ₹{money:,}")
    print("=" * 70)

if __name__ == "__main__":
    play_kbc()