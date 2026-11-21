import os
from PIL import Image

# Path to your labels folder and jpg folder
labels_path = 'C:/Users/hieut/FlickrLogos-v2/classes/label'
jpg_path = 'C:/Users/hieut/FlickrLogos-v2/classes/jpg'

# Class mapping from the updated data.yaml (replace with actual class IDs)
class_ids = {
    'adidas': 0,
    'aldi': 1,
    'apple': 2,
    'becks': 3,
    'bmw': 4,
    'carlsberg': 5,
    'chimay': 6,
    'cocacola': 7,
    'corona': 8,
    'dhl': 9,
    'erdinger': 10,
    'esso': 11,
    'fedex': 12,
    'ferrari': 13,
    'ford': 14,
    'fosters': 15,
    'google': 16,
    'guiness': 17,
    'heineken': 18,
    'hp': 19,
    'milka': 20,
    'nvidia': 21,
    'paulaner': 22,
    'pepsi': 23,
    'rittersport': 24,
    'shell': 25,
    'singha': 26,
    'starbucks': 27,
    'stellaartois': 28,
    'texaco': 29,
    'tsingtao': 30,
    'ups': 31
}

# Function to convert bounding box to YOLO format
def convert_to_yolo_format(x, y, w, h, img_w, img_h):
    center_x = (x + w / 2) / img_w
    center_y = (y + h / 2) / img_h
    width_norm = w / img_w
    height_norm = h / img_h
    return center_x, center_y, width_norm, height_norm

# Iterate through all label files
for subdir, _, files in os.walk(labels_path):
    for file in files:
        if file.endswith('.bboxes.txt'):
            file_path = os.path.join(subdir, file)
            
            # Extract the class name from the folder name (assuming folder names are class names)
            class_name = os.path.basename(os.path.dirname(file_path))
            class_id = class_ids.get(class_name, None)
            
            # Ensure that the class ID is found
            if class_id is None:
                print(f"Class ID for '{class_name}' not found!")
                continue
            
            # Construct the corresponding image file path in the 'jpg' folder
            # Extract the base name and remove `.bboxes.txt`
            image_name = os.path.basename(file).replace('.bboxes.txt', '')
            image_file = os.path.join(jpg_path, class_name, image_name)
            
            # If the image does not already end with .jpg, append .jpg to the filename
            if not image_file.endswith('.jpg'):
                image_file += '.jpg'

            # Check if the image file exists
            if not os.path.exists(image_file):
                print(f"Image file {image_file} not found!")
                continue
            
            # Open the image to get its dimensions
            with Image.open(image_file) as img:
                img_w, img_h = img.size  # Get image width and height
            
            # Open the .bboxes.txt file and read its contents
            with open(file_path, 'r') as bbox_file:
                lines = bbox_file.readlines()[1:]  # Skip the first header line

                # Prepare the output file in YOLO format
                yolo_file_path = file_path.replace('.bboxes.txt', '.txt')
                with open(yolo_file_path, 'w') as yolo_file:
                    for line in lines:
                        x, y, width, height = map(float, line.split())
                        
                        # Convert to YOLO format
                        center_x, center_y, width_norm, height_norm = convert_to_yolo_format(
                            x, y, width, height, img_w, img_h
                        )
                        
                        # Write the annotation in YOLO format
                        yolo_file.write(f"{class_id} {center_x} {center_y} {width_norm} {height_norm}\n")
            
            # Optionally delete the old .bboxes.txt file after conversion
            os.remove(file_path)
            print(f"Converted and deleted {file_path}")
