import io
import base64
import torch
import torch.nn as nn
import numpy as np
import segmentation_models_pytorch as smp
import albumentations as A
from albumentations.pytorch import ToTensorV2
from PIL import Image

# 1. FIXED MODEL DEFINITION
class MultiTaskUNet(nn.Module):
    def __init__(self, num_classes=5):
        # CORRECTED: Double underscores for __init__
        super(MultiTaskUNet, self).__init__() 
        
        # Matches '.pth' key: "base"
        self.base = smp.Unet(encoder_name="resnet50", encoder_weights=None, in_channels=3, classes=1)
        
        # Matches '.pth' key: "classifier"
        self.pool = nn.AdaptiveAvgPool2d((1, 1))
        self.classifier = nn.Sequential(
            nn.Flatten(),                # index 0
            nn.Linear(2048, 512),        # index 1
            nn.BatchNorm1d(512),         # index 2
            nn.ReLU(),                   # index 3
            nn.Dropout(0.4),             # index 4
            nn.Linear(512, num_classes)  # index 5
        )

    def forward(self, x):
        mask_out = self.base(x)
        features = self.base.encoder(x)[-1]
        class_out = self.classifier(self.pool(features))
        return mask_out, class_out

# Global State
MODEL_PATH = "brain_tumor_99plus_epoch_21.pth"
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
CLASSES = ["Normal", "Glioma", "Meningioma", "Pituitary", "Tumor"]
model = None

# Albumentations global val_transform
val_transform = A.Compose([
    A.Resize(224, 224),
    A.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ToTensorV2()
])

def load_model():
    global model
    try:
        print(f"Loading weights from {MODEL_PATH} onto {DEVICE}...")
        model = MultiTaskUNet(num_classes=len(CLASSES))
        
        state_dict = torch.load(MODEL_PATH, map_location=DEVICE)
        
        # Strip 'module.' prefix if it exists from Kaggle/Multi-GPU training
        if any(k.startswith('module.') for k in state_dict.keys()):
            state_dict = {k.replace('module.', ''): v for k, v in state_dict.items()}
            
        model.load_state_dict(state_dict)
        model.to(DEVICE)
        model.eval()
        print("✅ Success: Model and Weights Loaded!")
    except Exception as e:
        print(f"❌ Failed to load model: {e}")


def get_clinical_insights(class_name: str, confidence: float, mask_pixels: int) -> dict:
    # Descriptions mapping
    descriptions = {
        "Normal": "No abnormal masses detected in the active scan volume. The brain parenchyma appears unremarkable.",
        "Glioma": "Glioma is a primary brain tumor arising from glial cells. High-grade forms typically progress rapidly and aggressively.",
        "Meningioma": "Meningioma typically originates from the meninges. They are usually slow-growing and benign, but can cause localized pressure effects.",
        "Pituitary": "Pituitary adenoma is a benign tumor of the pituitary gland, often affecting hormonal balance and occasionally impinging the optic chiasm.",
        "Tumor": "Unspecified neoplastic mass detected within the cranial vault."
    }

    # Severity logic
    if mask_pixels < 800:
        base_severity = "Low"
    elif mask_pixels <= 2500:
        base_severity = "Moderate"
    else:
        base_severity = "High"

    severity = base_severity
    if confidence < 0.85:
        severity += " Borderline"

    # Priority logic
    if class_name == "Normal":
        priority = "Standard"
    elif base_severity == "Moderate":
        priority = "Elevated"
    elif base_severity == "High":
        priority = "Urgent"
    else:
        priority = "Standard" # Default for low non-normal

    # Next steps logic
    if class_name == "Normal":
        next_steps = ["Standard clinical follow-up", "No immediate neuro-radiological intervention indicated"]
    elif class_name == "Glioma":
        next_steps = ["Request full contrast-enhanced MRI", "Multidisciplinary neuro-oncology board review", "Assess for surgical resection viability"]
    elif class_name == "Meningioma":
        next_steps = ["Sequential volumetric monitoring", "Consider surgical excision if symptomatic", "Stereotactic radiosurgery assessment"]
    elif class_name == "Pituitary":
        next_steps = ["Comprehensive endocrine profile", "Visual field exam", "Referral to endocrinology"]
    else:
        next_steps = ["Pathological biopsy for definitive tissue diagnosis", "Advanced contrast imaging required"]

    return {
        "description": descriptions.get(class_name, "Analysis details unavailable."),
        "severity": severity,
        "priority": priority,
        "next_steps": next_steps
    }

def process_image(image_bytes: bytes):
    if model is None:
        raise RuntimeError("Model is not loaded. Ensure the .pth file exists.")
        
    # 1. Load image and convert to NumPy array (Albumentations format)
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    image_np = np.array(image)
    
    # 2. Apply Val Transform
    transformed = val_transform(image=image_np)
    input_tensor = transformed["image"].unsqueeze(0).to(DEVICE)
    
    # 3. Model Inference
    with torch.no_grad():
        mask_out, class_out = model(input_tensor)
        
        # Classification prediction
        probs = torch.softmax(class_out, dim=1)
        predicted_idx = torch.argmax(probs, dim=1).item()
        confidence = probs[0, predicted_idx].item()
        pred_class_name = CLASSES[predicted_idx]
        
        # Segmentation mask
        seg_mask = torch.sigmoid(mask_out)
        seg_mask = (seg_mask > 0.2).float()
        
        # Convert to 224x224 8-bit Numpy slice
        mask_np_out = (seg_mask[0, 0].cpu().numpy() * 255).astype(np.uint8)

    # Convert Numpy mask to Base64 PNG
    mask_image = Image.fromarray(mask_np_out, mode='L')
    mask_buffer = io.BytesIO()
    mask_image.save(mask_buffer, format="PNG")
    mask_b64 = base64.b64encode(mask_buffer.getvalue()).decode('utf-8')
    
    # Clinical Insights mapping using area volume and conf
    mask_pixels = np.count_nonzero(mask_np_out)
    insights = get_clinical_insights(pred_class_name, confidence, mask_pixels)

    return {
        "prediction": pred_class_name,
        "confidence": round(confidence, 4),
        "segmentation_mask_b64": mask_b64,
        "clinical_insights": insights
    }