# 🔍 AI Visual Search Engine

An AI-powered full-stack image search tool that uses a deep neural network to find and return visually similar images from the CIFAR-100 dataset.

![screenshot](preview.png)

---

## 🚀 Features

- Upload an image from your computer
- Extracts features using **ResNet18**
- Compares against the **CIFAR-100** dataset
- Returns **top 5 visually similar images**
- Built with **React (frontend)** and **Flask + PyTorch (backend)**

---

## 🛠 Tech Stack

- 💻 **Frontend**: React, JavaScript, JSX, CSS
- 🔥 **Backend**: Python, Flask, TorchVision, NumPy
- 📦 **Model**: ResNet18 (pretrained on ImageNet)
- 🖼 Dataset: CIFAR-100 (100 labeled classes)

---

## 🧪 How to Run

### ▶ Backend (Flask)

```bash
cd backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt  # or install Flask, torch, torchvision, etc.
python app.py
