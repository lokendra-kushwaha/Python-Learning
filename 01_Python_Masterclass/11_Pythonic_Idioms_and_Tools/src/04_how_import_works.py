"""
====================================================================================
⚙️ HOW 'import' WORKS UNDER THE HOOD IN PYTHON
====================================================================================
Description: When you type 'import math' or 'import requests', Python doesn't 
             just magically bring the code. It goes through a strict 3-step 
             architectural process.
====================================================================================
"""

def section_divider(title):
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")

section_divider("THE 3-STEP IMPORT MECHANISM")

"""
STEP 1: The Search (Checking the Cache)
---------------------------------------
Before searching your computer, Python looks inside 'sys.modules' (a dictionary 
in RAM). If the module was already imported by another file, it instantly uses 
the cached version to save time and memory.

STEP 2: The Compilation (Creating .pyc)
---------------------------------------
If the module is NOT in cache, Python finds the actual file (e.g., math.py). 
It then compiles this human-readable code into machine-level Bytecode.
(This is why you often see a hidden 'pycache' folder appear in your project!)

STEP 3: The Execution (Running the code)
---------------------------------------
Python executes the imported file from Top to Bottom. 
* IMPORTANT: This is exactly why we use the 'if name == "main":' block. 
  Without it, any test code (like print statements) inside the imported module 
  would automatically run during this step!
"""

import sys

section_divider("LIVE DEMONSTRATION")

# Let's prove that Python caches imported modules!
print("-> Importing the 'math' module...")
import math

print("\n-> Checking if 'math' is now cached in Python's memory (sys.modules):")
# sys.modules contains all currently loaded modules
is_cached = 'math' in sys.modules
print(f"   Is 'math' in RAM? : {is_cached}")

print("\n-> What happens if we import it again?")
import math
print("   (Nothing happens! Python bypassed Step 2 and 3 because it used the cache from Step 1)")