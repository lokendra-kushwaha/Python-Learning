"""
Secret Language Encoder & Decoder

A fun text-based game that encrypts and decrypts user messages based on custom rules.
- Words with 3 or fewer characters are reversed.
- Words with more than 3 characters have their first and last letters swapped,
  and 3 random characters appended to both the beginning and the end.

Created By: Lokendra Kushwaha
"""

import random

# Made these global constants (Tuples) so they don't get depleted like Sets
RANDOM_START = ("asd", "dfg", "lkj", "jhg", "zxc", "mnb", "qwe", "poi", "rty")
RANDOM_END = ("qaz", "wsx", "edc", "rfv", "rgb", "thn", "yjm", "ukl", "iop")

def encode(text):
    """Encodes English text into secret code."""
    words = text.split()
    encoded_words = []
    
    for word in words:
        if len(word) <= 3:
            encoded_words.append(word[::-1])
        else:
            # Using random.choice() instead of .pop() prevents the "empty set" crash
            r_start = random.choice(RANDOM_START)
            r_end = random.choice(RANDOM_END)
            
            # Swap first and last letter and attach random gibberish
            new_word = f"{r_start}{word[-1]}{word[1:-1]}{word[0]}{r_end}"
            encoded_words.append(new_word)
            
    return " ".join(encoded_words)

def decode(text):
    """Decodes the secret code back to English."""
    words = text.split()
    decoded_words = []
    
    for word in words:
        if len(word) <= 3:
            decoded_words.append(word[::-1])
        else:
            # Remove 3 chars from start and end using slicing
            core_word = word[3:-3]
            
            # Swap back the first and last letter of the core_word
            original_word = f"{core_word[-1]}{core_word[1:-1]}{core_word[0]}"
            decoded_words.append(original_word)
            
    return " ".join(decoded_words)

def main():
    print("Welcome to the Secret Language Generator! 🕵️‍♂️\n")
    
    while True:
        print("1. Encode English")
        print("2. Decode a Secret")
        print("3. Exit")
        user_input = input("--------> ").strip()
        
        if user_input == '1':
            text = input("\nEnter text to Encode: ")
            print(f"Your Secret Code: 👇\n{encode(text)}\n")
        
        elif user_input == '2':
            text = input("\nEnter text to Decode: ")
            print(f"Your English Sentence: 👇\n{decode(text)}\n")
            
        elif user_input == '3':
            print("Exiting... Keep your secrets safe!")
            break
            
        else:
            print("Invalid Input! Please select 1, 2, or 3.\n")

if __name__ == "__main__":
    main()