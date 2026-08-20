# 🍔 Restaurant Billing System

A straightforward command-line Python application that simulates a restaurant's order and billing system. This project was built during my early Python learning phase to practice data structures and control flow.

## ✨ Features
* **Interactive Ordering:** Users can continuously add items to their order until they type 'done'.
* **Menu Dictionary:** Uses a Python dictionary to store and look up menu items and their respective prices.
* **Dynamic Discount System:**
  * **0% Discount** for orders under 500 Rs.
  * **10% Discount** automatically applied for orders between 500 Rs and 999 Rs.
  * **20% Discount** automatically applied for orders of 1000 Rs or more.
* **Error Handling:** Gracefully handles invalid menu inputs, prompting the user to try again.

## 🧠 Concepts Demonstrated
* Dictionary lookups and iteration.
* while loops for continuous user input.
* Conditional logic (if-elif-else) for applying business rules (discounts).
* Modular code structure using functions.

## 🚀 How to Run
1. Ensure you have Python installed on your system.
2. Clone this repository and navigate to the project directory.
3. Run the script using the terminal:
   ``bash
   python billing_system.py
``
4. Follow the on-screen prompts to place your order!