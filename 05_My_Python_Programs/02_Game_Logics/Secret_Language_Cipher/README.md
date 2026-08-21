# 🕵️‍♂️ Secret Language Encoder & Decoder

A fun command-line game that converts standard English sentences into a custom "gibberish" cipher and can decode them back into readable English.

## 🧠 The Cipher Logic
The encryption runs on a custom set of string manipulation rules:
*   **Short Words (<= 3 characters):** Simply reversed (e.g., `dog` -> `god`).
*   **Long Words (> 3 characters):** 
    1. The first and last letters are swapped.
    2. Three random characters are appended to the start.
    3. Three random characters are appended to the end.
    *Example:* `python` -> `asd` + `n` + `ytho` + `p` + `qaz` = `asdnythopqaz`

## 🚀 Technical Features Highlighted
* **Advanced Slicing:** Demonstrates core Python string slicing techniques (`word[1:-1]`, `word[3:-3]`, `word[::-1]`).
* **Random Module:** Uses `random.choice()` for generating unpredictable cipher padding.
* **Modular Functions:** Keeps encoding and decoding logic cleanly separated from the main CLI loop.

## 💡 Developer's Fun Fact (The Legacy Logic)
When I originally built this project, I hadn't learned about Python's `random` module yet. To generate random gibberish, I stored the padding characters in a Python `Set`. Since sets are unordered, I used the `set.pop()` method to extract an arbitrary string every time! 

While it was a clever workaround, it had a bug: the script would crash if a sentence had more than 9 words (as the set would empty out). I have since upgraded the code to use the standard `random.choice()` from a Tuple, making it infinitely scalable and bug-free. This project stands as a great reminder of my growth and problem-solving journey!