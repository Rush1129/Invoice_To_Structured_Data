import cv2
import json
import numpy as np

# Load image and JSON label
image_path = "dataset/images/train/Template1_Instance0.jpg"  # Replace with actual invoice image path
label_path = "invoices_dataset/Annotations/Original_Format/Template1_Instance0.json"

image = cv2.imread(image_path)
height, width, _ = image.shape  # Get image dimensions

# Load label JSON
with open(label_path, "r") as f:
    labels = json.load(f)

# Define colors for different categories
colors = {
    "BUYER": (255, 0, 0),  # Blue
    "TOTAL": (0, 255, 0),  # Green
    "DATE": (0, 0, 255),   # Red
    "DISCOUNT": (128, 0, 128),  # Purple
}

# Iterate through JSON bounding boxes
for category, data in labels.items():
    if isinstance(data, list):  # If multiple bounding boxes
        for item in data:
            if "bbox" in item:
                (x1, y1), (x2, y2) = item["bbox"]

                # **Fix inverted bounding boxes**
                y1 = height - y1
                y2 = height - y2

                color = colors.get(category, (0, 255, 255))  # Default yellow
                cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)
                cv2.putText(image, category, (int(x1), int(y1) - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    elif isinstance(data, dict) and "bbox" in data:  # Single bounding box
        (x1, y1), (x2, y2) = data["bbox"]

        # **Fix inverted bounding boxes**
        y1 = height - y1
        y2 = height - y2

        color = colors.get(category, (0, 255, 255))
        cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)
        cv2.putText(image, category, (int(x1), int(y1) - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

# Save corrected image
cv2.imwrite("corrected_invoice_bbox.jpg", image)
print("Corrected bounding box image saved as corrected_invoice_bbox.jpg")
