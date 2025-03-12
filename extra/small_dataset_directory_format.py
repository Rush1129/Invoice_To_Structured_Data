import os
import shutil
import random

# Paths for full dataset
full_images_dir = "dataset/images/train"
full_labels_dir = "dataset/labels/train"

# Paths for small dataset
base_dir = "dataset_small"
split_dirs = ["train", "val", "test"]

# Create necessary directories
for split in split_dirs:
    os.makedirs(f"{base_dir}/images/{split}", exist_ok=True)
    os.makedirs(f"{base_dir}/labels/{split}", exist_ok=True)

# Get all image files
all_images = [f for f in os.listdir(full_images_dir) if f.endswith(".jpg")]

# Randomly select 50 images
small_subset = random.sample(all_images, 50)

# Split into train (70%), val (20%), test (10%)
train_split = small_subset[:35]
val_split = small_subset[35:45]
test_split = small_subset[45:]

# Function to copy images & labels
def copy_files(image_list, split):
    for img_name in image_list:
        label_name = img_name.replace(".jpg", ".txt")
        shutil.copy(os.path.join(full_images_dir, img_name), os.path.join(base_dir, "images", split, img_name))
        shutil.copy(os.path.join(full_labels_dir, label_name), os.path.join(base_dir, "labels", split, label_name))

# Copy files into respective splits
copy_files(train_split, "train")
copy_files(val_split, "val")
copy_files(test_split, "test")

print("Small dataset with `train`, `val`, and `test` splits created successfully!")
