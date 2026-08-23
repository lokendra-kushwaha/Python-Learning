"""
CLI English Vocabulary Builder 📖

A command-line dictionary tool that allows users to search for the 
meanings of complex English words. Demonstrates the use of Python 
dictionaries, while-loops, and string formatting.

Created By: Lokendra Kushwaha
"""

def main():
    # Dictionary containing words and their meanings
    my_dict = {
        'Sesquipedalian': 'Characterized by long words; long-winded.', 
        'Obfuscate': 'To make something unclear or obscure.', 
        'Grandiloquent': 'Pompous or extravagant in language, style, or manner, especially in a way that is intended to impress.', 
        'Recalcitrant': 'Having an obstinately uncooperative attitude toward authority or discipline.', 
        'Ephemeral': 'Lasting for a very short time.', 
        'Cacophony': 'A harsh, discordant mixture of sounds.', 
        'Sycophant': 'A person who acts obsequiously toward someone important in order to gain advantage.'
    }

    print("=" * 60)
    print("               📚 ADVANCED VOCABULARY DICTIONARY 📚               ")
    print("=" * 60)
    print("Available words to search: ")
    print(", ".join(my_dict.keys()))
    print("-" * 60)

    while True:
        # Taking input and formatting it to match dictionary keys
        user_meaning = input("\nEnter Word (or type 'exit' to quit): ").strip().title()
        
        if user_meaning.lower() == "exit":
            print("Keep learning new words! Goodbye. 👋")
            break 
            
        elif user_meaning in my_dict:
            print(f"📖 Meaning of '{user_meaning}': \n➔ {my_dict.get(user_meaning)}")
            
        else:
            print(f"❌ '{user_meaning}' is not present in this dictionary. Please try another word.")

if __name__ == "__main__":
    main()