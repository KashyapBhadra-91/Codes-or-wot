import os
import shutil

def copy_file_to_subdirectory(source_file, destination_dir):
    # Create the destination directory if it doesn't exist
    os.makedirs(destination_dir, exist_ok=True)

    # Get the filename from the source path
    filename = os.path.basename(source_file)

    # Construct full destination path
    destination_file = os.path.join(destination_dir, filename)

    # Copy the file
    shutil.copy2(source_file, destination_file)
    print(f"File '{filename}' copied to '{destination_dir}'.")

# Example usage
source_file = "source_folder/sample.txt"        
destination_dir = "new_folder/subfolder"        

copy_file_to_subdirectory(source_file, destination_dir)
