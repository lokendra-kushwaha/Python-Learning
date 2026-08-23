# 📖 Advanced English Vocabulary Builder

A terminal-based dictionary application that lets users search for the meanings of complex English words (like 'Grandiloquent' or 'Obfuscate').

## 💡 How It Works
The program displays a list of available complex words. The user types a word, and the program retrieves its meaning from a backend dictionary.

## 🛠️ Code Evolution & Logic
* **Data Structuring:** This is one of my earliest practical uses of Python **Dictionaries** (`{key: value}`) to map words to their respective definitions.
* **Robust Input Handling:** Utilizes string methods like `.strip()` and `.title()` to ensure that even if the user types in lowercase or adds extra spaces, the program still correctly matches the dictionary key.
* **Safe Retrieval:** Uses the `.get()` method to fetch data safely, preventing the script from crashing if an invalid word is entered.