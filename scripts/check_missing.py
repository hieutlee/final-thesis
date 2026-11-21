import os

# Paths to the images and labels directories
images_dir = 'C:/Users/hieut/FlickrLogos-v2/images/train'
labels_dir = 'C:/Users/hieut/FlickrLogos-v2/labels/train'

# Get list of all .jpg files (without extensions)
image_files = [os.path.splitext(f)[0] for f in os.listdir(images_dir) if f.endswith('.jpg')]

# Get list of all .txt files (without extensions)
label_files = [os.path.splitext(f)[0] for f in os.listdir(labels_dir) if f.endswith('.txt')]

# Check for images without corresponding labels
missing_labels = [f + '.jpg' for f in image_files if f not in label_files]

# Check for labels without corresponding images
missing_images = [f + '.txt' for f in label_files if f not in image_files]

# Report missing files
if missing_labels:
    print("Images without corresponding labels (.txt files):")
    for file in missing_labels:
        print(file)
else:
    print("No missing labels found. Every image has a corresponding label.")

if missing_images:
    print("\nLabels without corresponding images (.jpg files):")
    for file in missing_images:
        print(file)
else:
    print("No missing images found. Every label has a corresponding image.")
