# 🧮 Range-Based Prime Factorization

A pure mathematical script designed to find the prime factors of all numbers within a specific range provided by the user.

## 💡 Mathematical Logic
The script relies on a fundamental mathematical approach:
1. It iterates through the user's range using a `for` loop.
2. For each number, it starts dividing by the smallest prime number ($2$).
3. If the number is cleanly divisible (using the modulo operator `%`), it registers the factor and performs floor division (`//`) to reduce the number.
4. If not divisible, it increments the divisor and repeats the `while` loop until the number is reduced to $1$.

## 🛠️ Key Learnings
* Understanding nested loops: Using a `while` loop inside a `for` loop.
* Applying algorithmic thinking to solve core mathematical problems in Python without relying on external libraries.