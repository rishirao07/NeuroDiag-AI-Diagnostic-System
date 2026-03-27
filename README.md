---
title: NeuroDiag AI
emoji: 🧠
colorFrom: blue
colorTo: gray
sdk: docker
app_port: 7860
pinned: false
---

# NeuroDiag AI: Hybrid Multi-Task Brain Tumor Analysis System

![Medical AI](https://img.shields.io/badge/Status-Clinical--Ready-emerald) ![Python](https://img.shields.io/badge/Python-3.11-blue) ![PyTorch](https://img.shields.io/badge/Framework-PyTorch-orange) ![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688)

**NeuroDiag AI** is a professional diagnostic workstation designed to assist neurologists and radiologists in identifying brain pathologies. It utilizes a deep learning **Multi-Task U-Net** (ResNet-50 Backbone) to perform simultaneous classification and pixel-level segmentation across MRI and CT modalities.

---

## 📸 System Overview

### 1. Unified Diagnostic Interface
The primary workstation allows for seamless image uploads and real-time visualization.
![Frontend UI](./Frontend%20UI.png)

### 2. Multi-Task Segmentation & Classification
The AI identifies the tumor type and generates a pixel-perfect **Crimson Red** mask overlay to delineate boundaries.
![Segmented Results](./Segmented%20Results.png)

### 3. Clinical Insight Engine
Automated analysis provides the tumor description, severity grading, and academic next-step recommendations.
![Clinical Insights](./Description%20About%20The%20Tumor.png)

---

## 🚀 Core Achievements
* **Classification Accuracy:** Verified **97.40%** on hybrid clinical datasets.
* **Segmentation Precision:** Mean Dice Similarity Coefficient (DSC) of **0.8430**.
* **Architecture:** Shared ResNet-50 Encoder with specialized Dual-Head Decoders.
* **Dual-Modality:** Optimized for both MRI and CT analysis.

---

## 🛠️ Tech Stack
* **AI Framework:** PyTorch 2.x (Inference Engine)
* **Backbone:** ResNet-50 (Pre-trained)
* **Backend:** FastAPI (Asynchronous high-concurrency framework)
* **Frontend:** Industrial Light UI (Tailwind CSS, HTML5 Canvas API)

---

## 💻 Setup and Installation

### 1. Clone & Navigate
```bash
git clone [https://github.com/rishirao07/NeuroDiag-AI-Diagnostic-System.git](https://github.com/rishirao07/NeuroDiag-AI-Diagnostic-System.git)
cd NeuroDiag-AI-Diagnostic-System
```

### 2. Create Virtual Environment
```powershell
# We recommend Python 3.11 for maximum stability
uv venv --python 3.11
.\.venv\Scripts\activate
```

### 3. Install Dependencies
```powershell
pip install torch torchvision --index-url [https://download.pytorch.org/whl/cpu](https://download.pytorch.org/whl/cpu)
pip install fastapi uvicorn python-multipart segmentation-models-pytorch albumentations "numpy<2.0" "opencv-python-headless<4.10" pillow
```

---

## 🏃 Running the Application

### **Method: Failsafe Execution (Recommended for Windows)**
Launch the server using the direct environment path to ensure all library links are localized.

```powershell
# Run this once to allow the script to execute
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

# Launch the Diagnostic Engine
.\.venv\Scripts\python.exe -m uvicorn main:app --host 127.0.0.1 --port 8000
```

---

## 🛠️ Troubleshooting (Common Errors)

### **Error: Port 8000 is already in use (Errno 10048)**
If you see an error stating "only one usage of each socket address is normally permitted," it means a previous session is still holding the port.

**Solution: The "Clean Slate" Command**
Run this in PowerShell to force-close the hung process:
```powershell
Stop-Process -Id (Get-NetTCPConnection -LocalPort 8000).OwningProcess -Force
```
*After running this, you can immediately restart the application.*

---

## 📁 Repository Structure
```text
├── main.py                # FastAPI Router & Server Logic
├── inference.py           # Multi-Task Architecture & Inference Logic
├── index.html             # Industrial Light UI (HTML/CSS/JS)
├── brain_tumor_99plus_epoch_21.pth  # Serialized Model Weights (135MB)
├── Frontend UI.png        # UI Documentation
├── Segmented Results.png  # Analysis Documentation
└── Description About The Tumor.png # Insight Documentation
```

---

## ⚠️ Clinical Disclaimer
This software is a **Clinical Decision Support Tool** intended for research and educational purposes. All AI-generated findings must be reviewed and verified by a board-certified radiologist or medical professional before clinical action is taken.
```