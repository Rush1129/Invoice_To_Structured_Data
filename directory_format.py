import os
import shutil

# Define source and destination directories
source_images = "invoices_dataset/images"  # Folder containing all images
source_labels = "invoices_dataset/Annotations/YOLO_Format"  # Folder containing all labels

dest_images = "dataset/images"
dest_labels = "dataset/labels"

# Define split ratios
train_ratio = 0.8
val_ratio = 0.1
test_ratio = 0.1

# Ensure destination directories exist
for split in ["train", "val", "test"]:
    os.makedirs(os.path.join(dest_images, split), exist_ok=True)
    os.makedirs(os.path.join(dest_labels, split), exist_ok=True)

# Group images and labels by template
templates = {}
for filename in os.listdir(source_images):
    template_id = filename.split("_")[0].replace("Template", "")  # Extract numeric template ID
    if template_id not in templates:
        templates[template_id] = []
    templates[template_id].append(filename)

# Process each template and distribute images & labels
for template, files in templates.items():
    files.sort()  # Ensure order
    total = len(files)
    train_count = int(total * train_ratio)
    val_count = int(total * val_ratio)
    
    for i, file in enumerate(files):
        label_file = file.replace(".jpg", ".txt")  # Assuming label files have .txt extension
        
        if i < train_count:
            split = "train"
        elif i < train_count + val_count:
            split = "val"
        else:
            split = "test"
        
        shutil.copy(os.path.join(source_images, file), os.path.join(dest_images, split, file))
        shutil.copy(os.path.join(source_labels, label_file), os.path.join(dest_labels, split, label_file))

print("Dataset successfully split into train, val, and test!")

