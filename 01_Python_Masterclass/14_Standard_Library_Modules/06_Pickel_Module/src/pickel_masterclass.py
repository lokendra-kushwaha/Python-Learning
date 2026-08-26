"""
====================================================================================
🥒 STANDARD LIBRARY: THE 'pickle' MODULE
====================================================================================
Description: The 'pickle' module is used for serializing and de-serializing a Python 
             object structure. It converts complex Python objects into a byte stream 
             (0s and 1s) so they can be saved to a database or file, and then 
             restored perfectly later.

Crucial Difference from JSON:
1. JSON is text-based and cross-language (works in JS, Java, etc.).
2. Pickle is binary-based and Python-specific (only Python understands it).
3. JSON cannot save Custom Classes. Pickle CAN!
====================================================================================
"""

import pickle
import os

def section_divider(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")

# 🟢 1. THE TRUE POWER: Pickling Custom Objects
# ====================================================================================
section_divider("1. THE TRUE POWER: Serializing Custom Objects")

class GameCharacter:
    def __init__(self, name, level, health, inventory):
        self.name = name
        self.level = level
        self.health = health
        self.inventory = inventory
        
    def attack(self):
        return f"{self.name} attacks with {self.inventory[0]}!"

# Create an instance of our custom class
hero = GameCharacter("Lokendra", level=99, health=1000, inventory=["Sword", "Shield", "Potion"])

print(f"-> Original Object: {hero.name} (Level {hero.level})")
print(f"-> Action: {hero.attack()}")

# Serialize the entire object into bytes using pickle.dumps()
# Note: JSON would crash here!
pickled_bytes = pickle.dumps(hero)

print("\n-> Converted to Pickle Bytes (Looks like gibberish):")
print(pickled_bytes[:50], "...") # Printing only first 50 bytes


# 🟢 2. DESERIALIZATION: Restoring the Object
# ====================================================================================
section_divider("2. DESERIALIZATION: Restoring Objects from Bytes")

# Restore the object using pickle.loads()
restored_hero = pickle.loads(pickled_bytes)

print(f"-> Restored Object Type: {type(restored_hero)}")
print(f"-> Restored Name: {restored_hero.name}")
print(f"-> Can it still attack? : {restored_hero.attack()}")
print("   (Success! The object retained all its methods and properties!)")


# 🟢 3. FILE I/O: Saving Machine Learning Models / State (dump & load)
# ====================================================================================
section_divider("3. FILE I/O: Saving and Loading from Files")

file_path = "save_state.pkl" # .pkl is the standard extension for pickle files

# A. Writing to a file (MUST use 'wb' - Write Binary)
with open(file_path, "wb") as file:
    pickle.dump(hero, file)
print(f"   [+] Game state successfully saved to {file_path}")

# B. Reading from a file (MUST use 'rb' - Read Binary)
with open(file_path, "rb") as file:
    loaded_game_state = pickle.load(file)
print(f"   [+] Game state loaded! Welcome back, {loaded_game_state.name}.")

# Cleanup
os.remove(file_path)
print(f"   [-] Cleaned up {file_path}")


# 🟢 4. THE ARCHITECT'S WARNING: Security Risks
# ====================================================================================
section_divider("4. 🚨 CRITICAL SECURITY WARNING 🚨")
"""
Pickle is NOT secure against erroneous or maliciously constructed data.
NEVER unpickle data received from an untrusted source or over a public network.
A hacker can inject malicious Python code into a pickle file, and when you 
run pickle.load(), that code will execute on your server!
"""
print("-> RULE: Only unpickle files that you have generated yourself!")

print("\n" + "=" * 70)
print("🎯 CONCLUSION: Pickle is the ultimate tool for saving complex Python states.")
print("=" * 70)

# ====================================================================================
# 🎤 INTERVIEW QUESTION
# ====================================================================================
"""
Q: "When should we use JSON and when should we use Pickle to save data?"

Answer:
"Sir, the biggest difference lies in preserving the object's 'Identity'. 

When we serialize a custom Python Object using JSON, it loses its true identity 
(its class structure, specific data type, and methods) and is downgraded into a 
simple dictionary. JSON is great when we want to share this data with a web frontend 
or another language like JavaScript.

However, Pickle preserves the exact identity of the Python object. When we unpickle 
it, it returns as the exact same class instance with all its methods intact! 
Therefore, if I need to save a trained Machine Learning model or a pure Python 
application state, I will always use Pickle. 
(Though I will strictly avoid unpickling untrusted files to prevent code injection.)"
"""