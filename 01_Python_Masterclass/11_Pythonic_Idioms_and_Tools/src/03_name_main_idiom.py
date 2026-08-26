"""
====================================================================================
🐍 PYTHONIC IDIOMS: if __name__ == "__main__":
====================================================================================
Description: This special block allows a Python file to be used in two ways:
             1. As a standalone script (runs the main code).
             2. As an importable module (provides functions without running them).
====================================================================================
"""

def add_numbers(a, b):
    """A useful function that we might want to import into other files."""
    return a + b

def multiply_numbers(a, b):
    """Another useful function."""
    return a * b


# ====================================================================================
# 🛡️ THE SHIELD: Execution Control Block
# ====================================================================================
# Any code inside this 'if' block will ONLY run when this file is executed directly.
# It will NOT run if this file is imported by another script.

if __name__ == "__main__":
    print("\n🚀 [DIRECT EXECUTION] You are running this file directly!")
    print(f"   The secret variable name is set to: '{__name__}'\n")
    
    # We can safely test our functions here
    print("   Testing add_numbers(5, 10)      ->", add_numbers(5, 10))
    print("   Testing multiply_numbers(5, 10) ->", multiply_numbers(5, 10))
    
else:
    # This part runs ONLY when the file is imported elsewhere
    print(f"\n📦 [IMPORTED] This file was imported! The secret variable name is: '{__name__}'")
    print("   (The test codes were blocked from running.)\n")


# Short Answer: this set up gives you the option to run (or not run) a chunk of code when imported from another python file.