# 📺 KBC (Kaun Banega Crorepati) Simulator

A command-line trivia game simulating the famous Indian TV show "Kaun Banega Crorepati". 

## 🎮 Game Mechanics
* **10-Question Ladder:** The difficulty and prize money increase with each question, up to ₹7 Crores.
* **Milestone System:** Incorporates "Safe Havens". If a player answers incorrectly, they don't lose everything; they drop down to the last cleared milestone (₹10,000 or ₹2,00,00,000).
* **Walk Away Option:** The player can type `Q` at any point to quit the game and secure their current prize money.

## 🧠 Technical Architecture
* **Parallel Arrays/Lists:** Uses a 2D list for storing questions and options, while mapping them to a parallel 1D array (`levels`) for prize money distribution.
* **String Formatting:** Uses f-strings with comma formatting (e.g., `{money:,}`) to display large numbers gracefully (e.g., `10,000,000`).
* **Input Sanitization:** A robust `while` loop prevents crashes by strictly enforcing input choices (A/B/C/D/Q).