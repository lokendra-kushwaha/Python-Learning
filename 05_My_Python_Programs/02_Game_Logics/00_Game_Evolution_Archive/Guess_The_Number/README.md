# 🔢 Legacy Game: Hardcoded "Guess The Number"

This folder archives my very first version of the classic "Guess The Number" game. 

## 🧠 The Hardcoded Secret
Unlike standard versions of this game where a random number is generated for the user to guess, **this script has the winning number permanently hardcoded as `53`**. 
The hints provided by the game are strictly bound to ranges around the number 53 (e.g., if guess >= 70, print "Too High"). 

## 🛠️ Code Evolution Highlights
Looking back at this code, it's a perfect blend of beginner logic and surprisingly advanced syntax:
* **The Brute-Force:** Instead of using a single loop and adjusting the `total_chances` variable dynamically based on the difficulty, I copy-pasted the entire core loop three separate times for Easy, Medium, and Hard modes.
* **The Pythonic Spark:** Despite the copy-pasting, the code implements chained comparisons (`35 <= guess <= 52`) and effectively utilizes Python's lesser-known `for-else` construct to handle the "Game Over" condition without needing extra flag variables!

A true testament to the "make it work first, optimize later" mindset!