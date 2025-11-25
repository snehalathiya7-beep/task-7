
"""
Image Resizer Tool
------------------
This script resizes and converts images in batch.
Made using Python + Pillow.

Author: Sneha Lathiya
"""

import os
from PIL import Image

INPUT_FOLDER = "input_images"
OUTPUT_FOLDER = "output_images"
RESIZE_WIDTH = 800
RESIZE_HEIGHT = 800
OUTPUT_FORMAT = "JPEG"

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

def resize_images():
    print("Batch Image Resizing Started...\n")
    for filename in os.listdir(INPUT_FOLDER):
        if filename.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
            img_path = os.path.join(INPUT_FOLDER, filename)
            img = Image.open(img_path)
            img_resized = img.resize((RESIZE_WIDTH, RESIZE_HEIGHT))
            new_name = os.path.splitext(filename)[0] + "." + OUTPUT_FORMAT.lower()
            save_path = os.path.join(OUTPUT_FOLDER, new_name)
            img_resized.save(save_path, OUTPUT_FORMAT)
            print(f"✔ Resized: {filename} → {new_name}")
    print("\nDone! All images have been resized.")

if __name__ == "__main__":
    resize_images()
