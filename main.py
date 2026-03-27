from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import base64
import os

# Import the placeholder inference module
import inference

app = FastAPI(title="Brain Tumor Diagnostic API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    # Load the proxy model weights during startup
    inference.load_model()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    """
    Serve the main index.html file containing the frontend.
    """
    html_file = os.path.join(os.path.dirname(__file__), "index.html")
    if os.path.exists(html_file):
        with open(html_file, "r", encoding="utf-8") as f:
            return f.read()
    return HTMLResponse(content="<h1>index.html not found!</h1>", status_code=404)

@app.post("/api/predict")
async def predict(file: UploadFile = File(...)):
    """
    Endpoint for uploading Brain MRI or CT scans.
    Performs placeholder inference and returns classification logic
    with a base64 mask.
    """
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image.")

    try:
        image_bytes = await file.read()
        
        # Process the image through our inference placeholder module
        result = inference.process_image(image_bytes)
        
        return {
            "success": True,
            "filename": file.filename,
            "prediction": result["prediction"],
            "confidence": result["confidence"],
            "segmentation_mask_base64": result["segmentation_mask_b64"],
            "clinical_insights": result["clinical_insights"],
            "processing_time_ms": 120
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
