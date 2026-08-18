# ❌⭕ Tic-Tac-Toe Game Engine

A fully functional, terminal-based Tic-Tac-Toe game built with Python. This project features a clean Object-Oriented Programming (OOP) design, dynamic board rendering, and robust error handling to ensure a smooth gaming experience.

## ✨ Features
* **Two Game Modes:** 
  * 🧑‍🤝‍🧑 **Player vs Player:** Battle it out with a friend on the same computer.
  * 🤖 **Player vs Computer:** Test your skills against an AI opponent.
* **Smart AI:** The computer intelligently scans for available empty slots before making a move, ensuring optimal and valid gameplay.
* **Robust Error Handling:** Prevents crashes from invalid inputs (e.g., typing letters instead of numbers) and stops players from overwriting already filled boxes.
* **Clean Terminal UI:** A beautifully formatted 3x3 grid that updates dynamically after every turn.

## 🚀 How to Run

1. Make sure you have [Python](https://www.python.org/) installed on your system (Python 3.x recommended).
2. Clone this repository or download the source code.
3. Open your terminal or command prompt in the project folder.
4. Run the script using the following command:

```bash
python tic_tac_toe.py
```
*(Note: If you named your file differently, replace `tic_tac_toe.py` with your actual file name)*

## 🎮 How to Play

1. **Select Mode:** Upon starting, the game will ask you to choose a mode:
   * Type `1` for Player vs Player
   * Type `2` for Player vs Computer
2. **Setup:** Enter your name and choose your favorite mark (e.g., `X` or `O`). *(Note: The computer defaults to `#`)*.
3. **Make a Move:** The board is numbered from 1 to 9 (Top-Left to Bottom-Right). During your turn, simply type the number corresponding to the empty box where you want to place your mark.
   
   **Board Layout:**
```text
_____________
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
=============
```

4. **Winning:** The first player to get 3 of their marks in a row (horizontally, vertically, or diagonally) wins the game! If all 9 boxes are filled and no one has 3 in a row, the game ends in a Draw.

## 🏗️ Project Structure
This game is built using four main Python classes:
* `Board`: Manages the 3x3 grid, places marks, and checks for win/draw conditions.
* `Player`: Handles human player details and input validation.
* `Computer`: Manages the AI logic for generating valid random moves.
* `Game`: The core engine that manages the game loop, turns, and state.

---
*Built with ❤️ and Python.*