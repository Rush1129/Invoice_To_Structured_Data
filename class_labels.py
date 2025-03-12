import json
import os

# Paths
json_dir = "invoices_dataset/Annotations/Original_Format"

# Collect all unique class labels
all_labels = set()

# Scan all JSON files
for json_file in os.listdir(json_dir):
    if json_file.endswith(".json"):
        with open(os.path.join(json_dir, json_file), "r") as f:
            data = json.load(f)
        
        # Add all keys (class labels) to the set
        all_labels.update(data.keys())

# Defined class mapping (check if all labels exist)
class_mapping = {
    "TABLE": 0, "INVOICE_INFO": 1, "BUYER": 2, "DATE": 3,
    "NUMBER": 4, "NOTE": 5, "SELLER_EMAIL": 6, "SELLER_NAME": 7,
    "TOTAL": 8, "TOTAL_WORDS": 9, "GSTIN": 10, "LOGO": 11, "OTHER": 12
}

# Check if any missing labels exist
missing_labels = all_labels - set(class_mapping.keys())
extra_labels = set(class_mapping.keys()) - all_labels

# Print results
print(f"Unique labels found in dataset: {sorted(all_labels)}")
if missing_labels:
    print(f" Missing labels in class_mapping: {missing_labels}")
if extra_labels:
    print(f" Extra labels in class_mapping (not in dataset): {extra_labels}")
if not missing_labels:
    print("All labels match correctly!")
