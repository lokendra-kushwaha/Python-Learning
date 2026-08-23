# 💎 Custom Diamond Pattern

A clean and efficient Python script that generates a symmetric diamond pattern of asterisks (`*`) based on a user-defined height.

## 💡 The Logic Behind the Sparkle
Unlike traditional C or Java pattern printing that requires 3 nested loops (one for rows, one for spaces, one for stars), this script utilizes a much more **"Pythonic"** approach:
* **String Multiplication:** Using `(" " * spaces) + ("*" * stars)` to instantly generate the entire row's output in a single mathematical step.
* **Floor Division:** The spaces are dynamically calculated using `(n - i) // 2` to ensure the stars are always perfectly centered, regardless of how large the diamond gets.

It's a perfect example of how Python's built-in features can drastically reduce code complexity.