---
title: NeuroDiag AI
emoji: 🧠
colorFrom: blue
colorTo: gray
sdk: docker
app_port: 7860
pinned: false
---
This is the complete, updated `README.md` file. It now includes the **Failsafe / Client Deployment** section we just used, ensuring anyone who downloads the project (including your client) can run it regardless of their local Windows configuration.

```markdown
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

## 🚀 Core Achievements
* **Classification Accuracy:** Verified **97.40%** on hybrid clinical datasets.
* **Segmentation Precision:** Mean Dice Similarity Coefficient (DSC) of **0.8430**.
* **Architecture:** Shared ResNet-50 Encoder with specialized Dual-Head Decoders.
* **Dual-Modality:** Optimized for both MRI (soft-tissue) and CT (density-based) analysis.
* **Clinical Insight Engine:** Automated severity grading and clinical next-step directives.

---

## 🛠️ Tech Stack
* **AI Framework:** PyTorch 2.x (Inference Engine)
* **Backbone:** ResNet-50 (Pre-trained on ImageNet for spatial hierarchy).
* **Preprocessing:** Albumentations (Standardized clinical-grade augmentations).
* **Backend:** FastAPI (Asynchronous high-concurrency Python framework).
* **Frontend:** Industrial Light UI (Tailwind CSS, Vanilla JS, HTML5 Canvas API).
* **Image Processing:** OpenCV, PIL, NumPy (Optimized for <2.0 stability).

---

## 💻 Setup and Installation

### 1. Clone the Repository
```bash
git clone [https://github.com/rishirao07/NeuroDiag-AI-Diagnostic-System.git](https://github.com/rishirao07/NeuroDiag-AI-Diagnostic-System.git)
cd NeuroDiag-AI-Diagnostic-System
```

### 2. Create a Virtual Environment
Using a virtual environment is mandatory to prevent library conflicts (especially for NumPy and PyTorch).
```powershell
# Using standard Python
python -m venv .venv
.\.venv\Scripts\activate

# OR using 'uv' for high-speed setup
uv venv --python 3.11
.\.venv\Scripts\activate
```

### 3. Install Required Dependencies
We use a specific index for CPU-optimized PyTorch to keep the installation lightweight.
```powershell
# Install Torch CPU first
pip install torch torchvision --index-url [https://download.pytorch.org/whl/cpu](https://download.pytorch.org/whl/cpu)

# Install remaining requirements
pip install fastapi uvicorn python-multipart segmentation-models-pytorch albumentations "numpy<2.0" "opencv-python-headless<4.10" pillow
```

---

## 🏃 Running the Application

### **Method A: Standard (If Python is in PATH)**
```bash
uvicorn main:app --host 127.0.0.1 --port 8000
```

### **Method B: Failsafe / Client Deployment (Recommended for Windows)**
Use this method if the folder path contains spaces (e.g., `Major proj new`) or if Windows "App Aliases" interfere with the Python command.

1.  **Unlock PowerShell Execution Policy** (Run once as Administrator):
    ```powershell
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
    ```

2.  **Direct-Path Execution**:
    ```powershell
    # Launch using the environment's direct binary to bypass system pathing issues
    .\.venv\Scripts\python.exe -m uvicorn main:app --host 127.0.0.1 --port 8000
    ```

**Access the Dashboard:** Open your browser and go to `http://127.0.0.1:8000`.

---

## 📖 Usage Guide
1.  **Quick Start:** Click any image in the **'Sample Scans'** gallery to test the model instantly.
2.  **Upload:** Drag and drop a raw MRI or CT scan into the Scan Input box.
3.  **Run Inference:** Click the action button to process the scan (Average time: 120ms).
4.  **Analyze Results:**
    * **Dashboard:** Review the classification and confidence scores.
    * **Segmentation:** Toggle the **Crimson Red** mask overlay to verify tumor boundaries.
    * **Insights:** View rule-based severity levels and clinical recommendations.

---

## 📁 Repository Structure
```text
├── main.py                # FastAPI Router & Server Logic
├── inference.py           # Multi-Task Architecture & Inference Logic
├── index.html             # Industrial Light UI (HTML/CSS/JS)
├── requirements.txt       # Version-locked dependencies
├── brain_tumor_99plus_epoch_21.pth  # Serialized Model Weights (135MB)
└── Sample_MRI_images/     # Clinical test samples
```

---

## ⚠️ Clinical Disclaimer
This software is a **Clinical Decision Support Tool** intended for research and educational purposes. All AI-generated findings must be reviewed and verified by a board-certified radiologist or medical professional before clinical action is taken.
```