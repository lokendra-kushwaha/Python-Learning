"""
CLI Quiz Application

A multiple-choice quiz game featuring two scoring modes:
1. Normal Mode (+1 for correct, 0 for wrong)
2. Hard Mode (+1 for correct, -1/3 for wrong)

Created By: Lokendra Kushwaha
"""

def start_quiz():
    # Dictionary of Questions and Answers
    questions = {
        'Question-1: Which planet is known as the "Red Planet"?\nA) Venus  B) Jupiter  C) Mars  D) Saturn': 'C', 
        'Question-2: What is the capital of India?\nA) Mumbai  B) New Delhi  C) Kolkata  D) Chennai': 'B', 
        'Question-3: According to the Ramayana, what was the name of Lord Rama\'s father?\nA) Janaka  B) Ravana  C) Dasharatha  D) Valmiki': 'C',
        'Question-4: Which is the largest planet in our solar system?\nA) Earth  B) Mars  C) Saturn  D) Jupiter': 'D', 
        'Question-5: How many days are there in a week?\nA) 5  B) 6  C) 7  D) 8': 'C'
    }

    print("🧠 Welcome to the Ultimate Trivia Quiz! 🧠")
    print("Choose your Game Mode:")
    print("1. Normal Mode (No negative marking)")
    print("2. Hard Mode (Negative marking of 1/3 for each wrong answer)\n")
    
    # Mode Selection Logic
    while True:
        mode = input("Select Mode (1 or 2): ").strip()
        if mode in ['1', '2']:
            break
        print("Invalid Choice! Please enter 1 or 2.")
        
    print("-" * 60)
    
    score = 0
    negative_penalty = 0

    # Main Quiz Loop
    for question, answer in questions.items():
        print(f"\n{question}")
        
        # Input Validation Loop
        while True:
            user_input = input("Enter Your Option (A/B/C/D): ").upper().strip()
            if user_input in ['A', 'B', 'C', 'D']:
                break
            print("Invalid Input! Please type only A, B, C, or D.")

        # Checking the Answer
        if user_input == answer:
            score += 1
            print(f"✅ Correct! The answer is {answer}.")
        else:
            # If Hard Mode is selected, apply the 4/3 mathematical penalty logic
            if mode == '2':
                negative_penalty += (4/3) 
            print(f"❌ Wrong! You chose {user_input}, but the correct answer was {answer}.")

    print("\n" + "=" * 60)
    print("📋 FINAL RESULT")
    print("=" * 60)
    
    # Final Score Calculation
    total_q = len(questions)
    if mode == '2':
        # The advanced mathematical logic for negative marking
        final_score = total_q - negative_penalty
        # Rounding off to 2 decimal places for cleaner output
        print(f"Mode: Hard (Negative Marking)")
        print(f"Your Final Score is {round(final_score, 2)} out of {total_q}")
    else:
        # Standard scoring logic
        print(f"Mode: Normal")
        print(f"Your Final Score is {score} out of {total_q}")

if __name__ == "__main__":
    start_quiz()