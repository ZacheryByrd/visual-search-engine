import torch
import torchvision.transforms as transforms
import torchvision.datasets as datasets
import torchvision.models as models
import numpy as np
from PIL import Image
import pickle

# ----------------------------------------
# Load CIFAR-100 class names
# ----------------------------------------
def load_cifar100_class_names():
    with open('./cifar-100-python/meta', 'rb') as f:
        data = pickle.load(f, encoding='latin1')
    return data['fine_label_names']

class_names = load_cifar100_class_names()

# ----------------------------------------
# Load ResNet-18 (without final classifier)
# ----------------------------------------
def load_model():
    model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
    model.fc = torch.nn.Identity()  # remove classifier layer
    model.eval()
    return model

model = load_model()

# ----------------------------------------
# Image transform for ResNet input
# ----------------------------------------
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

# ----------------------------------------
# Load CIFAR-100 and extract embeddings
# ----------------------------------------
print("Loading CIFAR-100 dataset...")
cifar100_dataset = datasets.CIFAR100(
    root='./data',
    train=True,
    download=True,
    transform=transform
)

print("Extracting feature embeddings...")
database_embeddings = []
database_images = []

with torch.no_grad():
    for i, (img, label) in enumerate(cifar100_dataset):
        if i >= 100:  # limit to first 100 images
            break
        img_batch = img.unsqueeze(0)  # add batch dimension
        feature = model(img_batch).squeeze().numpy()
        database_embeddings.append(feature)
        database_images.append((img, label))

database_embeddings = np.array(database_embeddings)
print(f"✅ Loaded {len(database_embeddings)} images into database.")

# ----------------------------------------
# Similarity Search Function
# ----------------------------------------
def find_similar_images(query_img, top_k=5):
    img = transform(query_img).unsqueeze(0)
    with torch.no_grad():
        query_embedding = model(img).squeeze().numpy()

    similarities = database_embeddings @ query_embedding / (
        np.linalg.norm(database_embeddings, axis=1) * np.linalg.norm(query_embedding) + 1e-10
    )

    top_indices = np.argsort(similarities)[-top_k:][::-1]

    matches = []
    for idx in top_indices:
        img_tensor, label = database_images[idx]
        matches.append({
            'index': idx,
            'label': int(label),
            'class_name': class_names[int(label)],  # ✅ added here
            'similarity': float(similarities[idx])
        })

    return matches
