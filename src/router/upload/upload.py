
from fastapi import APIRouter, Depends
from src.schema.account import AccountBase
from src.dataaccess.account import account as data_access

# ml import in further
from fastapi import APIRouter, UploadFile, File, Form, HTTPException, Depends
# from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from app.services.auth_service import get_current_user
from app.services.ml_model import get_job_recommendations_from_bytes # Naya function
import fitz # PyMuPDF



router = APIRouter()







router = APIRouter(prefix="/api/user", tags=["User"])

@router.post("/recommend")
async def get_recommendations_on_upload(
    file: UploadFile = File(...), 
    current_user: dict = Depends(get_current_user)
):
    """
    Receives a resume file in-memory, processes it, and returns job recommendations directly.
    """
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")
    
    try:
        # Step 1: Read the file content into memory as bytes
        pdf_bytes = await file.read()
        
        # Step 2: Call the ML service with the bytes
        recommendations = get_job_recommendations_from_bytes(pdf_bytes)
        
        # Step 3: Return the recommendations
        return {"success": True, "data": recommendations}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred during processing: {str(e)}")