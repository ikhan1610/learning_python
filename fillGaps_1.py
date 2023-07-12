import os
import re

def close_numbering_gap(folder, prefix):
    # Get a list of all files in the folder
    files = os.listdir(folder)
    
    # Filter files that match the given prefix
    prefix_regex = re.compile(rf'^{re.escape(prefix)}(\d+)(\.\w+)$')
    matching_files = [file for file in files if prefix_regex.match(file)]
    
    # Sort the matching files in ascending order
    sorted_files = sorted(matching_files, key=lambda x: int(prefix_regex.match(x).group(1)))
    
    # Check for any numbering gaps and rename the subsequent files
    for i, file in enumerate(sorted_files):
        expected_number = i + 1
        current_number = int(prefix_regex.match(file).group(1))
        
        if current_number != expected_number:
            new_name = f'{prefix}{expected_number:03d}{os.path.splitext(file)[1]}'
            old_path = os.path.join(folder, file)
            new_path = os.path.join(folder, new_name)
            
            # Rename the file
            os.rename(old_path, new_path)
            print(f'Renamed "{file}" to "{new_name}"')
    
    print('Numbering gaps closed.')

# Example usage
folder = 'testFolder'  # Specify the folder path
prefix = 'spam'  # Specify the prefix of the files
close_numbering_gap(folder, prefix)
