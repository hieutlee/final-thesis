import os
import shutil

# Directories for images and labels in train and val
train_images_dir = 'C:/Users/hieut/FlickrLogos-v2/images/train'
val_images_dir = 'C:/Users/hieut/FlickrLogos-v2/images/val'
train_labels_dir = 'C:/Users/hieut/FlickrLogos-v2/labels/train'
val_labels_dir = 'C:/Users/hieut/FlickrLogos-v2/labels/val'

def move_file(src, dest):
    """Move file from src to dest."""
    if os.path.exists(src):
        print(f"Moving {src} to {dest}")
        shutil.move(src, dest)

def synchronize_files(images_dir, labels_dir, dest_images_dir, dest_labels_dir):
    """Ensure all files have corresponding .jpg and .txt files in the correct folders."""
    for file in os.listdir(images_dir):
        if file.endswith('.jpg'):
            base_name = os.path.splitext(file)[0]  # Get the filename without extension
            
            # Check if corresponding .txt file exists in the labels directory
            label_file = base_name + '.txt'
            label_path = os.path.join(labels_dir, label_file)
            image_path = os.path.join(images_dir, file)
            
            if not os.path.exists(label_path):  # If the label is missing
                print(f"Label file missing for {file}, moving {file} to validation")
                move_file(image_path, os.path.join(dest_images_dir, file))
            else:  # If the image is in the wrong folder, move both image and label
                correct_image_path = os.path.join(dest_images_dir, file)
                correct_label_path = os.path.join(dest_labels_dir, label_file)
                
                if not os.path.exists(correct_image_path):
                    move_file(image_path, correct_image_path)
                if not os.path.exists(correct_label_path):
                    move_file(label_path, correct_label_path)

def check_and_move_images():
    # Check train and val images and labels, moving files as needed
    print("Checking train images and labels...")
    synchronize_files(train_images_dir, train_labels_dir, val_images_dir, val_labels_dir)
    
    print("Checking validation images and labels...")
    synchronize_files(val_images_dir, val_labels_dir, train_images_dir, train_labels_dir)

# Run the synchronization
check_and_move_images()
