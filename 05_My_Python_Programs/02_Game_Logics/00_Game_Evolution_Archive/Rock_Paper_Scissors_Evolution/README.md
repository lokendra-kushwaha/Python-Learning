# 🪨📃✂️ Rock, Paper, Scissors: The Evolution

Welcome to the evolutionary timeline of my Rock, Paper, Scissors game! This folder serves as a time capsule, documenting how my problem-solving logic evolved from basic brute-force to creative data structures, and finally to clean conditional statements.

## 📂 Version History

### 1. Version 1: The Hardcoded Era (`v1_hardcoded_rps.py`)
* **The Logic:** The computer doesn't actually play; it follows a pre-written, hardcoded script for all 5 rounds.
* **Key Highlight:** Manual evaluation of all 5 rounds using separate `if-elif` blocks instead of a dynamic loop. It perfectly captures the "brute-force" phase of early learning.

### 2. Version 2: The Creative Pattern Array (`v2_pattern_array_rps.py`)
* **The Logic:** Introduced the `random` module! The computer finally makes unpredictable choices.
* **Key Highlight:** The **"Genius Hack"**. Before learning about Dictionaries or mathematical mapping, I created a 2D list containing all 9 possible outcomes (e.g., `['Rock', 'Paper', 'Loose']`). I then combined the user's and computer's choices into a list and matched it by slicing the master array `[0:2]`. A brilliant example of first-principles thinking!

### 3. Version 3: Compound Conditions (`v3_conditional_logic_rps.py`)
* **The Logic:** Abandoned the complex array slicing in favor of standard Pythonic compound conditions (`if X and Y`).
* **Key Highlight:** Highly readable and robust. It handles flexible user inputs (accepting both 'Rock' and 'R') and evaluates the game using standard logical operators. 

## 🚀 The Final Form
These three scripts laid the foundation for my understanding of logic building. Eventually, this evolution led me to write the ultimate mathematical version of this game (found in the main `Game_Logics` folder), where choices are mapped to `0, 1, 2` and evaluated using matrix-style arithmetic.