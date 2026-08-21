# 🐍💧🔫 Snake - Water - Gun Game

A Python terminal-based game replicating the childhood classic "Snake, Water, Gun" (a variation of Rock-Paper-Scissors). 

## 🎮 How to Play
The game runs for 5 rounds. You play against the computer.
* **Snake vs. Water:** Snake drinks the water. (Snake wins)
* **Water vs. Gun:** Water rusts the gun. (Water wins)
* **Gun vs. Snake:** Gun shoots the snake. (Gun wins)

## 🧠 Technical Highlights
* **Dictionary Logic:** Instead of relying on long, nested `if-elif-else` blocks, this project uses a Hash Map (Python Dictionary) to handle win conditions elegantly. The rule `Key defeats Value` is verified in a single `O(1)` check.
* **Input Sanitization:** A `while` loop continuously checks user input to ensure it perfectly matches the available options, preventing `KeyError` crashes.


## 🔄 Alternative Algorithmic Approach
Before implementing the dictionary-based logic, I initially solved this problem using a numerical state-mapping approach. By assigning integers to the choices (`0: Snake, 1: Water, 2: Gun`), I evaluated the win/loss matrix through distinct states.

```python
def check(comp, user):
    if comp == user:
        return 0  # Draw
    
    # Losing conditions for the user
    if (comp == 0 and user == 1) or (comp == 1 and user == 2) or (comp == 2 and user == 0):
        return -1 
        
    return 1      # User Wins
```
This highlights my ability to approach the same problem from both a "Data Structure" perspective and a traditional "Conditional Matrix" perspective.