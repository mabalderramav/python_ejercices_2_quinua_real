import os
from collections import Counter

import cv2
import matplotlib.pyplot as plt

# This script processes a dataset of images, extracting information about each image,
# analyzing the number of images per category, displaying example images, and plotting
# the distribution of image sizes.

# Define the path to the dataset
DATASET_PATH = './dataset'

# 1. Create a dictionary with image info
images = {}
for root, dirs, files in os.walk(DATASET_PATH):
    for file in files:
        if file.lower().endswith(('.jpg', '.jpeg', '.png')):
            path = os.path.join(root, file)
            category = os.path.basename(root)
            # Read the image to get its dimensions
            img = cv2.imread(path)
            # Check if the image was loaded successfully
            if img is not None:
                height, width = img.shape[:2]
                images[f"{category}_{file.title()}"] = {
                    'ruta': path,
                    'categoría': category,
                    'alto': height,
                    'ancho': width
                }

# 2. Analyze the number of images per category
category_counts = Counter([image_info['categoría'] for image_info in images.values()])
print("Images per category:", category_counts)

# 3. Show an example image per category
for category in category_counts:
    for image_category in images.values():
        if image_category['categoría'] == category:
            img = cv2.imread(image_category['ruta'])
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            plt.imshow(img_rgb)
            plt.title(f"Example: {category}")
            plt.axis('off')
            plt.show()
            break

# 4. Plot distribution of image sizes
heights = [image['alto'] for image in images.values()]
widths = [image['ancho'] for image in images.values()]
# Scatter plot of widths vs. heights
plt.scatter(widths, heights, alpha=0.5)
plt.xlabel('Width')
plt.ylabel('Height')
plt.title('Image Size Distribution')
plt.show()

# 5. Most and least frequent categories
most_common = category_counts.most_common(1)[0]
least_common = category_counts.most_common()[-1]
print(f"Most frequent category: {most_common[0]} ({most_common[1]} images)")
print(f"Least frequent category: {least_common[0]} ({least_common[1]} images)")