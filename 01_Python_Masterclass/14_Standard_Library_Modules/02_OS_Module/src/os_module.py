"""
====================================================================================
🖥️ STANDARD LIBRARY: THE 'os' MODULE (Operating System)
====================================================================================
Description: The 'os' module allows Python to interact with the underlying 
             Operating System (Windows, Mac, Linux). It is the backbone of 
             file management, directory navigation, and system automation.
====================================================================================
"""

import os
import time

def section_divider(title):
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")

# 🟢 1. NAVIGATION & DIRECTORIES
# ====================================================================================
section_divider("1. WHERE ARE WE? (Navigation)")

# getcwd() -> Get Current Working Directory
current_path = os.getcwd()
print(f"-> Current Working Directory : {current_path}")

# listdir() -> Shows everything inside a folder (like typing 'ls' or 'dir' in terminal)
print(f"-> Items in current folder   : {os.listdir(current_path)[:5]} ...") 


# 🟢 2. CROSS-PLATFORM PATHS (The Architect Way)
# ====================================================================================
section_divider("2. PATH JOINING (Cross-Platform Magic)")
"""
Why os.path.join? 
Windows uses backslashes (\), Mac/Linux use forward slashes (/). 
os.path.join automatically puts the correct slash depending on the user's OS!
"""
folder_name = "test_os_folder"
file_name = "secret_data.txt"

# Safe, professional way to combine paths
full_path = os.path.join(current_path, folder_name, file_name)
print(f"-> Professionally Joined Path: {full_path}")


# 🟢 3. CREATING AND DELETING (Automation)
# ====================================================================================
section_divider("3. AUTOMATION: CREATE & DELETE")

test_dir = os.path.join(current_path, folder_name)

# Create a directory if it doesn't exist
if not os.path.exists(test_dir):
    os.mkdir(test_dir)
    print(f"   [+] Created directory: {folder_name}")
else:
    print(f"   [*] Directory already exists: {folder_name}")

# Let's create a dummy file inside it
test_file_path = os.path.join(test_dir, "dummy_file.txt")
with open(test_file_path, "w") as f:
    f.write("This is temporary data.")
print("   [+] Created a dummy file inside the folder.")

print("   ⏳ Waiting 2 seconds before cleaning up...")
time.sleep(2)

# Cleanup: Delete file, then delete folder (Cannot delete a folder if it has files!)
os.remove(test_file_path)
print("   [-] Deleted the dummy file.")

os.rmdir(test_dir)
print("   [-] Deleted the directory. Workspace is clean!")


# 🟢 4. ENVIRONMENT VARIABLES (Advanced / Production)
# ====================================================================================
section_divider("4. ENVIRONMENT VARIABLES (Security)")
"""
Real-world apps never hardcode passwords. They read them from the OS environment.
"""
# Reading an existing system variable (like USERNAME or PATH)
user = os.environ.get("USERNAME") or os.environ.get("USER")
print(f"-> Logged in OS User: {user}")

print("\n" + "=" * 60)
print("🎯 CONCLUSION: 'os' gives you complete control over the filesystem!")
print("=" * 60)