import cv2
import numpy as np

# Load Image
image_path = "dataset/images/train/Template30_Instance0.jpg"
label_path = "invoices_dataset/Annotations/YOLO_Format/Template30_Instance0.txt"  # YOLO label file

image = cv2.imread(image_path)
height, width, _ = image.shape  # Get image dimensions

# Read YOLO label file
with open(label_path, "r") as f:
    lines = f.readlines()

# Define a color map for different classes
color_map = {
    0: (255, 0, 0),  # Class 0 -> Blue
    1: (0, 255, 0),  # Class 1 -> Green
    2: (0, 0, 255),  # Class 2 -> Red
    3: (128, 0, 128),  # Class 3 -> Purple
}

# Parse and draw bounding boxes
for line in lines:
    parts = line.strip().split()
    class_id = int(parts[0])  # First value is class ID
    x_center, y_center, w, h = map(float, parts[1:])

    # Convert YOLO format to bounding box (x1, y1, x2, y2)
    x1 = int((x_center - w / 2) * width)
    y1 = int((y_center - h / 2) * height)
    x2 = int((x_center + w / 2) * width)
    y2 = int((y_center + h / 2) * height)

    

    # Get color based on class ID
    color = color_map.get(class_id, (0, 255, 255))  # Default Yellow

    # Draw rectangle and label
    cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
    cv2.putText(image, f"Class {class_id}", (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

# Save corrected image
cv2.imwrite("corrected_invoice_yolo.jpg", image)
print("Corrected YOLO bounding box image saved as corrected_invoice_yolo.jpg")
