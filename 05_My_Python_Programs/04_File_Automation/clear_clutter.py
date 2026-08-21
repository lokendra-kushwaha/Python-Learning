"""
Clear the Clutter (Bulk File Renamer)

A utility script to automatically bulk-rename files in a specific directory.
It scans for files with a specific extension and renames them sequentially 
(e.g., 1.png, 2.png, 3.png) to organize cluttered folders.

Created By: Lokendra Kushwaha
"""

import os

def clear_clutter(folder_path, ext):
    """
    Renames all files with a specific extension in a given folder sequentially.
    
    Args:
        folder_path (str): The absolute or relative path to the target folder.
        ext (str): The file extension to target (e.g., '.png', 'pdf').
        
    Returns:
        None
    """
    # Safety Check 1: Ensure the extension starts with a '.'
    if not ext.startswith('.'):
        ext = f".{ext}"

    # Safety Check 2: Check if the folder actually exists
    if not os.path.exists(folder_path):
        print(f"Error: The folder '{folder_path}' does not exist.")
        return

    try:
        # Fetching all files dynamically from the provided folder path
        all_files = os.listdir(folder_path)
        count = 1
        
        print(f"\nScanning '{folder_path}' for '{ext}' files...")
        
        for file in all_files:
            # Converting to lower case to handle cases like '.PNG' and '.png'
            if file.lower().endswith(ext.lower()):
                
                # os.path.join is safer than f"{folder_path}/{file}" for different OS
                old_path = os.path.join(folder_path, file)
                new_path = os.path.join(folder_path, f"{count}{ext}")
                
                # Prevent renaming if the name is already exactly what we want
                if old_path != new_path:
                    # Prevent overwriting if a file like '1.png' already exists
                    if not os.path.exists(new_path):
                        os.rename(old_path, new_path)
                        print(f"Renamed: '{file}'  ->  '{count}{ext}'")
                    else:
                        print(f"Skipped: '{count}{ext}' already exists. Attempting next number.")
                        count += 1
                        continue # Skip to next iteration to try next number
                
                count += 1
                
        print("-" * 50)
        print(f"Operation completed! Processed {count - 1} files.")
        print("-" * 50)
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# ==========================================
# Example Usage
# ==========================================
if __name__ == "__main__":
    # Ensure you have a folder named 'test_folder' with some dummy files before running
    # clear_clutter('test_folder', '.docx')
    # clear_clutter('test_folder', 'pdf') # The code will auto-add the '.' if missed
    pass