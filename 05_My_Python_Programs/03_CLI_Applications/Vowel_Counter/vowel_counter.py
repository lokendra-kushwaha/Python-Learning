"""
Vowel & Consonant Counter 🔠

A simple CLI utility to analyze a given string and count the 
total number of vowels and consonants. Demonstrates string iteration 
and conditional logic.

Created By: Lokendra Kushwaha
"""

def main():
    print("=" * 50)
    print("       🔠 WORD ANALYZER (VOWELS & CONSONANTS) 🔠       ")
    print("=" * 50)

    # Taking input from the user
    user_input = input("\nEnter a word or sentence: ").strip()
    
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0
    consonant_count = 0

    print("\nAnalyzing letters...")
    print("-" * 50)

    # Iterating through each character
    for char in user_input.lower():
        # Check if it's an alphabet letter
        if char.isalpha():
            if char in vowels_list:
                print(f"Found Vowel: '{char}'")
                vowel_count += 1
            else:
                consonant_count += 1

    print("-" * 50)
    print(f"📊 Results for: '{user_input.title()}'")
    print(f"Total Vowels    : {vowel_count}")
    print(f"Total Consonants: {consonant_count}")
    print("=" * 50)

if __name__ == "__main__":
    main()