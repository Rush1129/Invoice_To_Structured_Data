# import json
# import os

# # Paths
# json_dir = "invoices_dataset/Annotations/Original_Format"
# output_dir = "invoices_dataset/Annotations/YOLO_format"

# # Ensure output directory exists
# os.makedirs(output_dir, exist_ok=True)

# # Fixed image dimensions
# img_width, img_height = 595, 841  # All images have the same size

# # Class mapping
# class_mapping = {
#     "TABLE": 0, "INVOICE_INFO": 1, "BUYER": 2, "DATE": 3, "NUMBER": 4, "NOTE": 5, 
#     "SELLER_EMAIL": 6, "SELLER_NAME": 7, "TOTAL": 8, "TOTAL_WORDS": 9, "GSTIN": 10, 
#     "LOGO": 11, "OTHER": 12, "TAX": 13, "DISCOUNT": 14, "BILL_TO": 15, "GST(7%)": 16, 
#     "PO_NUMBER": 17, "SELLER_SITE": 18, "SELLER_ADDRESS": 19, "GST(12%)": 20, 
#     "SUB_TOTAL": 21, "GST(5%)": 22, "CONDITIONS": 23, "GSTIN_SELLER": 24, 
#     "TITLE": 25, "GST(9%)": 26, "SEND_TO": 27, "GST(1%)": 28, "GSTIN_BUYER": 29, 
#     "PAYMENT_DETAILS": 30, "GST(18%)": 31, "GST(20%)": 32, "AMOUNT_DUE": 33, 
#     "DUE_DATE": 34
# }

# # Convert annotations
# for json_file in os.listdir(json_dir):
#     if json_file.endswith(".json"):
#         with open(os.path.join(json_dir, json_file), "r") as f:
#             data = json.load(f)

#         print(f"Processing: {json_file}")  # Debugging step
#         yolo_annotations = []
        
#         # Convert each labeled object
#         for label, objects in data.items():
#             if label not in class_mapping:
#                 print(f"Skipping unknown label: {label}")  # Debugging output
#                 continue  # Skip unrecognized labels

#             if isinstance(objects, list):  # Case 1: List of objects (e.g., "TABLE")
#                 for obj in objects:
#                     if isinstance(obj, dict) and "bbox" in obj:
#                         bbox = obj["bbox"]
#                     elif isinstance(obj, list) and len(obj) > 0 and isinstance(obj[0], dict) and "bbox" in obj[0]:
#                         bbox = obj[0]["bbox"]  # Handle nested list case
#                     else:
#                         print(f"Skipping {label}, invalid 'bbox' format")  # Debugging output
#                         continue
                    
#                     # Extract coordinates
#                     x_min, y_min = bbox[0]
#                     x_max, y_max = bbox[1]

#                     # Normalize values
#                     x_center = ((x_min + x_max) / 2.0) / img_width
#                     y_center = ((y_min + y_max) / 2.0) / img_height
#                     width = (x_max - x_min) / img_width
#                     height = (y_max - y_min) / img_height

#                     yolo_annotations.append(f"{class_mapping[label]} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}")

#             elif isinstance(objects, dict) and "bbox" in objects:  # Case 2: Single dictionary (e.g., "BUYER")
#                 bbox = objects["bbox"]
                
#                 # Extract coordinates
#                 x_min, y_min = bbox[0]
#                 x_max, y_max = bbox[1]

#                 # Normalize values
#                 x_center = ((x_min + x_max) / 2.0) / img_width
#                 y_center = ((y_min + y_max) / 2.0) / img_height
#                 width = (x_max - x_min) / img_width
#                 height = (y_max - y_min) / img_height

#                 yolo_annotations.append(f"{class_mapping[label]} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}")

#         # Save in YOLO format
#         yolo_filename = json_file.replace(".json", ".txt")
#         with open(os.path.join(output_dir, yolo_filename), "w") as f:
#             f.write("\n".join(yolo_annotations))

# print("JSON annotations converted to YOLO format successfully!")

# import json
# import os

# # Paths
# json_dir = "invoices_dataset/Annotations/Original_Format"
# output_dir = "invoices_dataset/Annotations/YOLO_format"

# # Ensure output directory exists
# os.makedirs(output_dir, exist_ok=True)

# # Fixed image dimensions
# img_width, img_height = 595, 841  # All images have the same size

# # Class mapping
# class_mapping = {
#     "TABLE": 0, "INVOICE_INFO": 1, "BUYER": 2, "DATE": 3, "NUMBER": 4, "NOTE": 5, 
#     "SELLER_EMAIL": 6, "SELLER_NAME": 7, "TOTAL": 8, "TOTAL_WORDS": 9, "GSTIN": 10, 
#     "LOGO": 11, "OTHER": 12, "TAX": 13, "DISCOUNT": 14, "BILL_TO": 15, "GST(7%)": 16, 
#     "PO_NUMBER": 17, "SELLER_SITE": 18, "SELLER_ADDRESS": 19, "GST(12%)": 20, 
#     "SUB_TOTAL": 21, "GST(5%)": 22, "CONDITIONS": 23, "GSTIN_SELLER": 24, 
#     "TITLE": 25, "GST(9%)": 26, "SEND_TO": 27, "GST(1%)": 28, "GSTIN_BUYER": 29, 
#     "PAYMENT_DETAILS": 30, "GST(18%)": 31, "GST(20%)": 32, "AMOUNT_DUE": 33, 
#     "DUE_DATE": 34
# }

# # Function to normalize bbox coordinates
# def normalize_bbox(bbox, img_width, img_height):
#     """Converts bounding box coordinates to YOLO format and ensures positive width/height."""
#     x_min, y_min = bbox[0]
#     x_max, y_max = bbox[1]

#     # Compute normalized values
#     x_center = ((x_min + x_max) / 2.0) / img_width
#     y_center = ((y_min + y_max) / 2.0) / img_height
#     width = abs((x_max - x_min) / img_width)  # Ensure width is positive
#     height = abs((y_max - y_min) / img_height)  # Ensure height is positive

#     # Ensure valid YOLO format values
#     if width <= 0 or height <= 0:
#         return None  # Skip invalid bounding boxes

#     return f"{x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}"

# # Convert annotations
# for json_file in os.listdir(json_dir):
#     if json_file.endswith(".json"):
#         json_path = os.path.join(json_dir, json_file)
#         with open(json_path, "r", encoding="utf-8") as f:
#             data = json.load(f)

#         print(f"Processing: {json_file}")  # Debugging step
#         yolo_annotations = []

#         # Convert each labeled object
#         for label, objects in data.items():
#             if label not in class_mapping:
#                 print(f"Skipping unknown label: {label}")  # Debugging output
#                 continue  # Skip unrecognized labels

#             class_id = class_mapping[label]

#             if isinstance(objects, list):  # Case 1: List of objects
#                 for obj in objects:
#                     if isinstance(obj, dict) and "bbox" in obj:
#                         bbox_str = normalize_bbox(obj["bbox"], img_width, img_height)
#                         if bbox_str:
#                             yolo_annotations.append(f"{class_id} {bbox_str}")
#                     elif isinstance(obj, list) and len(obj) > 0 and isinstance(obj[0], dict) and "bbox" in obj[0]:
#                         bbox_str = normalize_bbox(obj[0]["bbox"], img_width, img_height)
#                         if bbox_str:
#                             yolo_annotations.append(f"{class_id} {bbox_str}")

#             elif isinstance(objects, dict) and "bbox" in objects:  # Case 2: Single dictionary
#                 bbox_str = normalize_bbox(objects["bbox"], img_width, img_height)
#                 if bbox_str:
#                     yolo_annotations.append(f"{class_id} {bbox_str}")

#         # Save in YOLO format only if annotations exist
#         if yolo_annotations:
#             yolo_filename = json_file.replace(".json", ".txt")
#             with open(os.path.join(output_dir, yolo_filename), "w", encoding="utf-8") as f:
#                 f.write("\n".join(yolo_annotations))

# print("JSON annotations converted to YOLO format successfully!")


import json
import os

# Paths
json_dir = "invoices_dataset/Annotations/Original_Format"
output_dir = "invoices_dataset/Annotations/YOLO_format"

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Fixed image dimensions (as per dataset info)
img_width, img_height = 595, 841  # All images have the same size

# Class mapping
class_mapping = {
    "TABLE": 0, "INVOICE_INFO": 1, "BUYER": 2, "DATE": 3, "NUMBER": 4, "NOTE": 5, 
    "SELLER_EMAIL": 6, "SELLER_NAME": 7, "TOTAL": 8, "TOTAL_WORDS": 9, "GSTIN": 10, 
    "LOGO": 11, "OTHER": 12, "TAX": 13, "DISCOUNT": 14, "BILL_TO": 15, "GST(7%)": 16, 
    "PO_NUMBER": 17, "SELLER_SITE": 18, "SELLER_ADDRESS": 19, "GST(12%)": 20, 
    "SUB_TOTAL": 21, "GST(5%)": 22, "CONDITIONS": 23, "GSTIN_SELLER": 24, 
    "TITLE": 25, "GST(9%)": 26, "SEND_TO": 27, "GST(1%)": 28, "GSTIN_BUYER": 29, 
    "PAYMENT_DETAILS": 30, "GST(18%)": 31, "GST(20%)": 32, "AMOUNT_DUE": 33, 
    "DUE_DATE": 34
}

# Function to normalize bbox coordinates (with Y-axis flipping)
def normalize_bbox(bbox, img_width, img_height):
    """Converts bounding box coordinates to YOLO format and flips Y-axis."""
    x_min, y_min = bbox[0]
    x_max, y_max = bbox[1]

    # **Flip the Y-axis coordinates**
    y_min = img_height - y_min
    y_max = img_height - y_max

    # Ensure correct bbox ordering after flipping
    y_min, y_max = min(y_min, y_max), max(y_min, y_max)

    # Compute YOLO normalized values
    x_center = ((x_min + x_max) / 2.0) / img_width
    y_center = ((y_min + y_max) / 2.0) / img_height
    width = abs((x_max - x_min) / img_width)  # Ensure width is positive
    height = abs((y_max - y_min) / img_height)  # Ensure height is positive

    # Ensure valid YOLO format values
    if width <= 0 or height <= 0:
        return None  # Skip invalid bounding boxes

    return f"{x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}"

# Convert annotations with corrected Y-axis
for json_file in os.listdir(json_dir):
    if json_file.endswith(".json"):
        json_path = os.path.join(json_dir, json_file)
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        print(f"Processing: {json_file}")  # Debugging step
        yolo_annotations = []

        # Convert each labeled object
        for label, objects in data.items():
            if label not in class_mapping:
                print(f"Skipping unknown label: {label}")  # Debugging output
                continue  # Skip unrecognized labels

            class_id = class_mapping[label]

            if isinstance(objects, list):  # Case 1: List of objects
                for obj in objects:
                    if isinstance(obj, dict) and "bbox" in obj:
                        bbox_str = normalize_bbox(obj["bbox"], img_width, img_height)
                        if bbox_str:
                            yolo_annotations.append(f"{class_id} {bbox_str}")
                    elif isinstance(obj, list) and len(obj) > 0 and isinstance(obj[0], dict) and "bbox" in obj[0]:
                        bbox_str = normalize_bbox(obj[0]["bbox"], img_width, img_height)
                        if bbox_str:
                            yolo_annotations.append(f"{class_id} {bbox_str}")

            elif isinstance(objects, dict) and "bbox" in objects:  # Case 2: Single dictionary
                bbox_str = normalize_bbox(objects["bbox"], img_width, img_height)
                if bbox_str:
                    yolo_annotations.append(f"{class_id} {bbox_str}")

        # Save in YOLO format only if annotations exist
        if yolo_annotations:
            yolo_filename = json_file.replace(".json", ".txt")
            with open(os.path.join(output_dir, yolo_filename), "w", encoding="utf-8") as f:
                f.write("\n".join(yolo_annotations))

print("JSON annotations converted to YOLO format successfully with corrected Y-axis!")
