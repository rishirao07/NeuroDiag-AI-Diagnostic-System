# NeuroDiag AI: Hybrid Multi-Task Brain Tumor Analysis System

![Medical AI](https://img.shields.io/badge/Status-Clinical--Ready-emerald) ![Python](https://img.shields.io/badge/Python-3.11-blue) ![PyTorch](https://img.shields.io/badge/Framework-PyTorch-orange) ![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688)

**NeuroDiag AI** is a professional diagnostic workstation designed to assist neurologists and radiologists in identifying brain pathologies. It utilizes a deep learning **Multi-Task U-Net** to perform simultaneous classification and pixel-level segmentation across MRI and CT modalities.

---

## 🚀 Core Achievements
* **Classification Accuracy:** Verified **97.40%** on hybrid datasets.
* **Segmentation Precision:** Mean Dice Similarity Coefficient (DSC) of **0.8430**.
* **Architecture:** ResNet-50 Encoder + Multi-Task U-Net Decoder.
* **Dual-Modality:** Optimized for both MRI (soft-tissue) and CT (density-based) analysis.
* **Clinical Insight Engine:** Automated severity grading and academic clinical recommendations.

---

## 🛠️ Tech Stack
* **AI Framework:** PyTorch (Inference Engine)
* **Backbone:** ResNet-50 (Pre-trained on ImageNet)
* **Preprocessing:** Albumentations (Standardized Clinical Augmentations)
* **Backend:** FastAPI (Asynchronous Python Framework)
* **Frontend:** Industrial Light UI (Tailwind CSS, Vanilla JS, HTML5 Canvas)
* **Image Processing:** OpenCV, PIL, NumPy 1.26.4 (Optimized for AI Stability)

---

## 💻 Setup and Installation (For Other Laptops)

Follow these steps to set up a clean, synchronized environment on any Windows/Mac/Linux machine.

### 1. Clone the Repository
```bash
git clone [https://github.com/rishirao07/NeuroDiag-AI-Diagnostic-System.git](https://github.com/rishirao07/NeuroDiag-AI-Diagnostic-System.git)
cd NeuroDiag-AI-Diagnostic-System
```

### 2. Create a Virtual Environment (Highly Recommended)
This prevents library version conflicts (like the NumPy 2.0 issue).
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Dependencies
```bash
pip install fastapi uvicorn python-multipart torch torchvision segmentation-models-pytorch albumentations "numpy<2.0" "opencv-python-headless<4.10" pillow
```

---

## 🏃 Running the Application
Launch the server using Uvicorn:
```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```
**Access the Dashboard:** Open your browser and go to `http://127.0.0.1:8000`.

---

## 📖 Usage Guide
1.  **Quick Start:** Click any image in the **'Sample Scans'** gallery to test the model instantly.
2.  **Upload:** Drag and drop a raw MRI or CT scan into the Scan Input box.
3.  **Run Inference:** Click the action button to process the scan.
4.  **Analyze Results:**
    * **Dashboard:** Review the classification and solid-blue confidence bar.
    * **Segmentation:** Toggle the **Crimson Red** mask overlay to see the tumor boundary.
    * **Insights:** View the rule-based severity level (Low/Moderate/High) and academic next-step directives.

---

## 📁 Repository Structure
```text
├── main.py              # FastAPI Router & Server Logic
├── inference.py         # AI Inference, Architecture, & Insight Engine
├── index.html           # Professional Medical UI
├── requirements.txt     # Locked Dependency Versions
├── samples/             # Clinical test images (MRI_1, CT_1, etc.)
└── *.pth                # Trained Weights (Epoch 21 - 97.4% Acc)
```

## ⚠️ Clinical Disclaimer
This software is a **Clinical Decision Support Tool** intended for research and educational purposes. All AI-generated findings must be reviewed and verified by a board-certified radiologist or medical professional before clinical action is taken.
```

