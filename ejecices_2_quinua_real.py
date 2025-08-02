import os
import cv2
import matplotlib.pyplot as plt
from collections import defaultdict, Counter

# Update this path to your extracted dataset folder
DATASET_PATH = 'dataset'

# 1. Create a dictionary with image info
image_dict = {}
for root, dirs, files in os.walk(DATASET_PATH):
    for file in files:
        if file.lower().endswith(('.jpg', '.jpeg', '.png')):
            path = os.path.join(root, file)
            category = os.path.basename(root)
            img = cv2.imread(path)
            if img is not None:
                h, w = img.shape[:2]
                image_dict[file] = {
                    'ruta': path,
                    'categoría': category,
                    'alto': h,
                    'ancho': w
                }

# 2. Analyze the number of images per category
category_counts = Counter([v['categoría'] for v in image_dict.values()])
print("Images per category:", category_counts)

# 3. Show an example image per category
for category in category_counts:
    for v in image_dict.values():
        if v['categoría'] == category:
            img = cv2.imread(v['ruta'])
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            plt.imshow(img_rgb)
            plt.title(f"Example: {category}")
            plt.axis('off')
            plt.show()
            break

# 4. Plot distribution of image sizes
heights = [v['alto'] for v in image_dict.values()]
widths = [v['ancho'] for v in image_dict.values()]
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