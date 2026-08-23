# 🧮 Armstrong Number Logic

This folder contains Python scripts dedicated to calculating and verifying Armstrong numbers (also known as Narcissistic numbers).

## 💡 The Mathematical Concept
An Armstrong number is a number that equals the sum of its digits, each raised to a power equal to the total number of digits.
* **Example (153):** It has 3 digits. 
  Calculation: `1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153`. (It is an Armstrong number).
* **Example (10):** It has 2 digits. 
  Calculation: `1^2 + 0^2 = 1 + 0 = 1`. `1 != 10`. (Not an Armstrong number).

## 🛠️ Code Execution & Logic
Instead of using complex modulus (`% 10`) and division (`// 10`) operators to extract digits mathematically, this code utilizes a very **"Pythonic" string-manipulation approach**:
1. The numbers are converted to strings (`str(number)`).
2. A `for` loop iterates through each character of the string.
3. The characters are converted back to integers on the fly to perform the exponentiation (`int(digit) ** length`).

This approach makes the code much shorter and easier to read while achieving the exact same mathematical result!