"""
====================================================================================
📦 STANDARD LIBRARY: THE 'shutil' MODULE (Shell Utilities)
====================================================================================
Description: While 'os' handles basic filesystem operations, 'shutil' is designed 
             for high-level operations on files and collections of files. 
             It is the go-to module for copying, moving, and archiving (Zipping) 
             entire directory trees.
====================================================================================
"""

import os
import shutil
import time

def section_divider(title):
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")

# ====================================================================================
# 🛠️ SETUP: Creating a safe temporary workspace
# ====================================================================================
workspace = "shutil_temp_workspace"
source_folder = os.path.join(workspace, "source")
dest_folder = os.path.join(workspace, "destination")

# Ensure workspace is clean before we start
if os.path.exists(workspace):
    shutil.rmtree(workspace)

os.makedirs(source_folder)
dummy_file = os.path.join(source_folder, "data.txt")

with open(dummy_file, "w") as f:
    f.write("This is highly confidential data!")
    
print(f"🛠️ Setup Complete: Created '{source_folder}' with a dummy file inside.")


# 🟢 1. COPYING FILES
# ====================================================================================
section_divider("1. COPYING FILES (shutil.copy2)")
"""
Note: shutil.copy() copies just the data. 
shutil.copy2() copies the data PLUS the metadata (like creation date, modified time).
Architects always prefer copy2!
"""
copied_file = os.path.join(source_folder, "data_backup.txt")
shutil.copy2(dummy_file, copied_file)

print(f"-> Copied file to: {copied_file}")
print(f"   Files in source now: {os.listdir(source_folder)}")


# 🟢 2. COPYING ENTIRE FOLDERS (Directory Trees)
# ====================================================================================
section_divider("2. COPYING ENTIRE FOLDERS (shutil.copytree)")
"""
If a folder has 100 sub-folders and files, copytree() copies ALL of them 
in a single command!
"""
shutil.copytree(source_folder, dest_folder)

print(f"-> Copied entire '{source_folder}' to '{dest_folder}'")
print(f"   Files in destination: {os.listdir(dest_folder)}")


# 🟢 3. MOVING & RENAMING
# ====================================================================================
section_divider("3. MOVING / RENAMING (shutil.move)")
"""
shutil.move() acts like 'Cut & Paste'. It is also the standard way to rename 
a folder or file in Python.
"""
renamed_folder = os.path.join(workspace, "renamed_destination")
shutil.move(dest_folder, renamed_folder)

print(f"-> Moved/Renamed destination folder to: {renamed_folder}")
print(f"   Current folders in workspace: {os.listdir(workspace)}")


# 🟢 4. ZIPPING FOLDERS (Archiving)
# ====================================================================================
section_divider("4. CREATING ZIP ARCHIVES (shutil.make_archive)")

archive_name = os.path.join(workspace, "my_backup")
# This creates my_backup.zip containing everything inside 'renamed_folder'
shutil.make_archive(base_name=archive_name, format="zip", root_dir=renamed_folder)

print(f"-> Created ZIP file: {archive_name}.zip")


# 🟢 5. THE DANGEROUS DELETE (Cleanup)
# ====================================================================================
section_divider("5. THE NUKE: DELETING FOLDERS (shutil.rmtree)")
"""
os.rmdir() crashes if a folder is not empty. 
shutil.rmtree() deletes the folder AND everything inside it permanently. Use with extreme caution!
"""
print("   ⏳ Waiting 3 seconds so you can verify the folders in your system...")
time.sleep(3)

# Deleting the entire workspace (Folders, Files, and Zips)
shutil.rmtree(workspace)
print(f"-> [DELETED] The '{workspace}' folder and all its contents have been wiped out.")
print("\n" + "=" * 60)
print("🎯 CONCLUSION: 'shutil' makes heavy file operations a piece of cake!")
print("=" * 60)

# ====================================================================================
# 🎤 DEVELOPER INTERVIEW QUESTION
# ====================================================================================
"""
Q: "Why do we need 'shutil.rmtree()' to delete a folder when we already 
    have 'os.rmdir()' in the OS module?"

Answer:
"Sir, 'os.rmdir()' is a safe but limited function. It can ONLY delete a folder 
if it is completely EMPTY. If there is even a single hidden file inside that 
folder, os.rmdir() will crash and throw an OSError.

On the other hand, 'shutil.rmtree()' is a Recursive function (like a bulldozer). 
It goes inside the target folder, deletes every single file and sub-folder one 
by one, and finally deletes the main folder itself. It handles non-empty 
directories effortlessly."
"""