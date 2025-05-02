# 🔍 AI Visual Search Engine

This is a full-stack AI-powered image similarity search tool.

### 💡 Features
- Upload any image
- Extract features using ResNet18 (PyTorch)
- Compare with CIFAR-100 dataset
- View top-5 visually similar images
- React + Flask architecture

### 🛠 Tech Stack
- React (frontend)
- Flask + PyTorch (backend)
- ResNet18 from torchvision
- CIFAR-100 dataset

### 🚀 How to Run

```bash
# In /backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python app.py
