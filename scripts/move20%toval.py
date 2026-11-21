import os
import shutil
import random

# Paths to your train and val directories
train_images_dir = 'C:/Users/hieut/FlickrLogos-v2/images/train'
val_images_dir = 'C:/Users/hieut/FlickrLogos-v2/images/val'
train_labels_dir = 'C:/Users/hieut/FlickrLogos-v2/labels/train'
val_labels_dir = 'C:/Users/hieut/FlickrLogos-v2/labels/val'

def move_file(src, dest):
    """Move file from src to dest if it exists."""
    if os.path.exists(src):
        shutil.move(src, dest)

# Get all .jpg files in the train folder
image_files = [f for f in os.listdir(train_images_dir) if f.endswith('.jpg')]

# Calculate 20% of the files to move back to val
num_files_to_move = int(len(image_files) * 0.2)

# Randomly select 20% of the image files to move back to val
files_to_move = random.sample(image_files, num_files_to_move)

# Move the selected files (both images and labels) back to val
for file in files_to_move:
    # Move image
    image_src = os.path.join(train_images_dir, file)
    image_dest = os.path.join(val_images_dir, file)
    move_file(image_src, image_dest)
    
    # Move corresponding label
    base_name = os.path.splitext(file)[0]  # Remove '.jpg'
    label_src = os.path.join(train_labels_dir, base_name + '.txt')
    label_dest = os.path.join(val_labels_dir, base_name + '.txt')
    move_file(label_src, label_dest)

print(f"Moved {num_files_to_move} images and their labels back to val.")
