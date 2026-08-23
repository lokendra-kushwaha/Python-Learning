# 🔠 Vowel & Consonant Analyzer

A text-analysis CLI application that takes a word or sentence from the user and calculates the exact number of vowels and consonants it contains.

## 💡 The Objective
To build a tool that can iterate through strings and categorize letters based on specific conditions.

## 🛠️ Code Architecture
* **String Iteration:** Uses a `for` loop to break down the user's input into individual characters for analysis.
* **List Checking:** Employs the `in` operator against a predefined list of vowels (`['a', 'e', 'i', 'o', 'u']`) to categorize each letter.
* **Data Validation:** Uses the `.isalpha()` method to ensure that numbers, spaces, or special characters are ignored during the counting process.