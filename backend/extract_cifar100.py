import pickle
import os
import numpy as np
from PIL import Image

def unpickle(file):
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='latin1')
    return dict

def save_images(data_dict, folder, start_index=0):
    images = data_dict['data']
    labels = data_dict['fine_labels']

    if not os.path.exists(folder):
        os.makedirs(folder)

    for i in range(100):  # limit to 100 images for testing
        img = images[i].reshape(3, 32, 32).transpose(1, 2, 0)
        img = Image.fromarray(img)
        filename = os.path.join(folder, f"{start_index + i}.png")
        img.save(filename)
        print(f"Saved {filename}")  # ✅ debug print


# Paths
train_data = unpickle('./cifar-100-python/train')
test_data = unpickle('./cifar-100-python/test')

# Output folder
output_folder = './converted_images'

# Save images (first 100 only for now)
save_images(train_data, output_folder, start_index=0)

print("✅ Finished extracting 100 images.")

