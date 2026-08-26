# 📦 The shutil Module: Shell Utilities

## 📌 Overview
While the os module handles basic file system tasks, shutil (Shell Utilities) is the "Heavy Machinery" designed for high-level operations on collections of files. It is the go-to tool for copying, moving, and archiving entire directory trees.

## 🚀 Core Capabilities
*   **Deep Copying:** shutil.copy2() copies not just the data, but also the metadata (creation date, modified time).
*   **Directory Trees:** shutil.copytree() can copy a folder along with hundreds of sub-folders and files in a single command.
*   **Archiving:** Easily compress folders into ZIP or TAR files using shutil.make_archive().
*   **The Bulldozer Delete:** shutil.rmtree() forcefully deletes a folder and everything inside it.

## 🎤 Interview Cheat-sheet
**Q: What is the difference between os.rmdir() and shutil.rmtree()?**
*   os.rmdir() is safe but limited; it only deletes **empty** folders. It crashes if a hidden file exists.
*   shutil.rmtree() is recursive. It acts like a bulldozer, going inside the target directory, deleting all contents one by one, and finally wiping the main folder itself.