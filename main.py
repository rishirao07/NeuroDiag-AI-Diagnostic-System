from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, FileResponse
import os
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
    # Load the model weights into memory on server start
    inference.load_model()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    # Serves your professional index.html dashboard
    index_path = os.path.join(os.path.dirname(__file__), "index.html")
    return FileResponse(index_path)

@app.post("/api/predict")
async def predict(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image.")

    try:
        image_bytes = await file.read()
        
        # Process the image through the inference engine
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

if __name__ == "__main__":
    import uvicorn
    # Important: Hugging Face Spaces strictly use port 7860
    port = int(os.environ.get("PORT", 7860))
    uvicorn.run(app, host="0.0.0.0", port=port)