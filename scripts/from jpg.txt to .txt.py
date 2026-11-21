import os

# Path to your labels folder
labels_path = 'C:/Users/hieut/FlickrLogos-v2/classes/label'

# Iterate through all files in the labels folder
for subdir, _, files in os.walk(labels_path):
    for file in files:
        # Check if the file ends with '.jpg.txt'
        if file.endswith('.jpg.txt'):
            old_file_path = os.path.join(subdir, file)
            # Create the new file name by replacing '.jpg.txt' with '.txt'
            new_file_path = old_file_path.replace('.jpg.txt', '.txt')

            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {old_file_path} -> {new_file_path}")

print("All files renamed successfully!")
