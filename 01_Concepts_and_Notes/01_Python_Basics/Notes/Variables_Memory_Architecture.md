# 📂 Python Primitive Data Types & Memory Architecture

Hey! In this section, we aren't just looking at basic data types on the surface. We are diving deep into how Python (CPython) actually stores and manages basic data types like integers, strings, floats, and complex numbers under the hood in RAM.

---

## 🚀 What's Inside This Folder?

### 1. Integers (`int`): The Unlimited Number Magic
* **No Overflow Limits:** Unlike C or Java where integers have fixed sizes (and crash if they exceed a certain limit), Python integers can be as massive as your RAM allows. Python breaks large numbers into chunks and stores them in a C-array behind the scenes.
* **Small Integer Caching:** Python is smart. It knows numbers from **-5 to 256** are used constantly. When Python starts, it pre-allocates these numbers in memory. If you write `a = 10` and `b = 10`, they both point to the exact same memory box instead of creating new ones.

### 2. Strings (`str`): The Ninja Trick of String Interning
* Strings store text data, but Python optimizes them aggressively.
* **String Interning:** If you create two separate variables with the exact same string (e.g., `a = "Lokendra"` and `b = "Lokendra"`), Python doesn't duplicate it in memory. It creates it once and points both variables to the same memory address.
* Every string also carries its length and hash code pre-calculated, so operations like `len()` happen instantly.

### 3. Floats (`float`): The IEEE 754 Precision Flaw
* Floats handle decimal numbers (like `3.14` or `0.1`). Python stores them as standard 8-byte (64-bit) C doubles.
* **The `0.1 + 0.2 != 0.3` Scam:** Computers only understand binary (0s and 1s). Just like $1/3$ results in a repeating decimal ($0.3333...$) in human math, numbers like `0.1` and `0.2` become infinite repeating fractions in binary. The computer chops them off to save space, leaving behind a tiny rounding error (giving `0.30000000000000004`).
* **The Fix:** If you need absolute financial accuracy, you use Python's built-in `Decimal` module instead of regular floats.

### 4. Complex Numbers (`complex`): Built-in Math
* Python natively supports complex numbers in the format `a + bj` (where `j` is imaginary). 
* Under the hood, Python simply stores them as two side-by-side float numbers in memory (one for the Real part, and one for the Imaginary part). This is heavily used in scientific computing and machine learning.

---

## 📁 Folder Structure
* **`code/`** $\rightarrow$ Contains all my practice `.py` scripts for primitive data types.
* **`notes/`** $\rightarrow$ Contains deep-dive documentation on memory allocation, garbage collection, and float precision issues.

---
*💡 Note: True engineering is not just about knowing syntax—it's about understanding how things work under the hood!*