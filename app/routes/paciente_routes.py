from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.patient import Patient
from app.routes.auth_routes import get_current_user

router = APIRouter()

@router.get("/patients")
async def get_patients(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    patients = db.query(Patient).all()
    return patients

@router.get("/patients/{patient_id}")
async def get_patient(patient_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Patient not found")
    return patient