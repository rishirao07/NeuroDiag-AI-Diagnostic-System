# Brain Tumor Multi-Task Diagnostic System

This is a professional, medical-grade web application for processing MRI and CT scans to automatically classify brain tumors and provide a multi-task segmentation overlay for tumor masks.

## Features
- **FastAPI Backend**: Asynchronous backend configured to run high-performance AI inference. 
- **Vanilla HTML5 + Tailwind CSS**: Zero-dependency UI (from a build step perspective), utilizing ES6 JavaScript, the HTML5 File API and HTML5 `<canvas>`.
- **Multi-Task U-Net Interface**: Backend modules designed to interface directly with PyTorch multi-task networks.
- **Segmentation Overlay**: Renders backend-encoded masks as a graphical overlay directly onto the brain scans for doctors.

## Prerequisites

- **Python 3.9+**
- (Optional but Recommended) A virtual environment like `venv` or `conda`

## Setup and Installation

1. Open your terminal in the project directory.
2. Install the necessary pip packages:
```bash
pip install fastapi uvicorn python-multipart torch torchvision pillow numpy
```

*(Note: Install the official `torch` wheel linked for your CUDA version if you plan on using GPU hardware).*

## Running the Application

To run the local development server:

```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

- Navigate your browser to: [http://127.0.0.1:8000](http://127.0.0.1:8000).
- The `index.html` frontend will load directly from the single executable instance.

## Usage Guide
1. Create or test a sample Brain CT / MRI image.
2. **Drag and Drop** the image file into the dashed box on the left.
3. Click "Run Inference" to send the packet to the U-Net representation.
4. Review the returned Patient clinical dashboard, confidence score, and toggle the interactive segmentation mask visualizer.
