import os
import re

# Get the folder where this script is running
folder_path = os.getcwd()

# Regex to find "Lecture" followed by a number
# It is case insensitive (re.IGNORECASE) just to be safe
pattern = re.compile(r"Lecture\s+(\d+)", re.IGNORECASE)

print(f"Scanning folder: {folder_path}...\n")

count = 0

for filename in os.listdir(folder_path):
    # Skip the script file itself
    if filename.endswith(".py"):
        continue

    # Search for the lecture number in the filename
    match = pattern.search(filename)
    
    if match:
        original_number = match.group(1)
        
        # .zfill(2) adds a zero to single digits (e.g., "5" -> "05")
        # If you have more than 100 lectures, change 2 to 3.
        sorted_number = original_number.zfill(2)
        
        # Check if file is already renamed to avoid duplicates (e.g. "05 05 Video...")
        if filename.startswith(sorted_number):
            continue

        # Create the new name: "05 - Original Name"
        # I added a dash " - " for cleaner looking files, you can remove it if you want.
        new_name = f"{sorted_number} - {filename}"
        
        old_file_path = os.path.join(folder_path, filename)
        new_file_path = os.path.join(folder_path, new_name)
        
        try:
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {new_name}")
            count += 1
        except Exception as e:
            print(f"Error renaming {filename}: {e}")

if count == 0:
    print("\nNo matching files found or files are already renamed.")
else:
    print(f"\nSuccess! {count} files were renamed.")

input("\nPress Enter to exit.")