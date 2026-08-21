# 🧹 Clear the Clutter (Bulk File Renamer)

Welcome to the **Clear the Clutter** utility script! 

This program is a handy automation tool built to organize messy folders. If you have a directory filled with randomly named files (e.g., downloaded images, scattered documents), this script will bulk-rename them sequentially (like `1.png`, `2.png`, `3.png`) based on their specific file extensions.

## ✨ Key Features
* **Dynamic Path Handling:** Utilizes `os.path.join` to ensure the script works flawlessly across all operating systems (Windows, macOS, Linux) without slash conflicts.
* **Smart Extension Parsing:** Automatically handles missing dots in user input (e.g., treats `png` as `.png`) and ignores case-sensitivity (`.PNG` vs `.png`).
* **Overwrite Protection:** Safely checks if a target file name (like `1.png`) already exists before renaming, preventing accidental data loss or file replacement.

## 🚀 How to Use
You can use this script to clean up any folder on your system. Just call the `clear_clutter()` function with the target folder path and the file extension.

```python
# Import the function
from clear_clutter import clear_clutter

# Example 1: Renaming all PNG images in a folder named 'assets'
clear_clutter('assets', '.png')

# Example 2: Renaming all PDF files in a specific Windows directory
clear_clutter('C:/Users/Username/Downloads/Documents', 'pdf') 
```

## 🧠 Core Concepts Highlighted
* File system manipulation using Python's built-in `os` module.
* Defensive programming (input sanitization and pre-execution safety checks).
* Automating repetitive, real-world tasks using loops and string formatting.