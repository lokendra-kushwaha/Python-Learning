# 🐍🪜 Snake and Ladder Game Engine

Welcome to the classic **Snake and Ladder Game**, fully re-imagined for the terminal using Python! 

This project is a fantastic showcase of **Object-Oriented Programming (OOP)**. It features a dynamically updating 10x10 grid, multiple difficulty levels, and supports both multiplayer and AI-based single-player modes.

## ✨ Key Features
* **Multiple Game Modes:** 
  * 🧑‍🤝‍🧑 **Player vs Player (PvP):** Play locally with a friend.
  * 🤖 **Player vs Computer (PvE):** Test your luck against an automated AI.
* **3 Difficulty Levels:**
  * 🟢 **Easy:** Standard board with a balanced number of snakes and ladders.
  * 🟡 **Medium:** Increased number of hazards to make the climb tougher.
  * 🔴 **Hard:** Brutal snake placements (Watch out for the snake at 99 that drops you down to 2!).
* **Dynamic Board Rendering:** A clean, constantly updating 10x10 terminal board that visually tracks player movements (`X` and `O`).
* **Overlap Handling:** If both players land on the same square, the game smartly displays both marks together (e.g., `"X""O"`).

## 🚀 How to Run

1. Ensure you have Python installed (Python 3.x recommended).
2. Clone this repository or download the Python file.
3. Open your terminal or command prompt in the folder containing the script.
4. Run the script:
```bash
python snake_and_ladder.py
```

## 🎮 How to Play

1. Start the game and choose your Mode (PvP or PvE) and Difficulty Level (Easy, Medium, Hard).
2. Players will take turns rolling a 6-sided dice. (Just press `Enter` to roll).
3. **Movement Rules:**
   * You start at position 0 (off the board).
   * **Ladders (`L`):** Landing on a ladder's bottom will instantly climb you up.
   * **Snakes (`S`):** Landing on a snake's head will slide you down to its tail.
4. **Winning:** You must land *exactly* on square **100** to win. If your dice roll takes you past 100, your turn is skipped until you roll the exact number needed!

---

## 🏗️ Project Architecture (Under the Hood)

For developers looking at the code, this project heavily utilizes **Inheritance** to keep the code clean (DRY principle). Here is how the logic is structured:

### 1. Board Classes
* `EasyBoard` (Base Class): Generates the 100-square list, places 'S' and 'L', and handles the `__str__` method for the 10x10 grid printing.
* `MediumBoard` & `HardBoard`: Inherit from `EasyBoard` but override the `__init__` method to inject different, more difficult snake and ladder dictionaries.

### 2. Player Classes
* `Player` (Base Class): Handles human interaction, asking for user input to roll the dice and managing the current/old positions.
* `Computer`: Inherits from `Player` but overrides the `dice_roll()` method to automate the dice rolling using Python's `random.randint`, removing the need for `input()`.

### 3. Game Engine Classes
* `EasyUserGame` (Base Logic): This is the core engine. It manages the `while` loop, turn switching, overlap logic, and checks for snakes/ladders/wins.
* All other game modes (e.g., `MediumComputerGame`, `HardUserGame`) inherit from `EasyUserGame`. They simply override the `__init__` method to load the correct Board and Player types, while reusing the complex `game_play()` loop logic from the base class!

---
*Built with ❤️, Logic, and Python.*