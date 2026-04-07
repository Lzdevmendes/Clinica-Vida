from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.services.patient_service import PatientService
from app.schemas.patient_schema import PatientResponse, PatientCreate, PatientUpdate
from app.routes.auth_routes import get_current_user

router = APIRouter()

@router.get("/patients", response_model=List[PatientResponse])
async def get_patients(
    skip: int = Query(0, ge=0, description="Records to skip"),
    limit: int = Query(20, ge=1, le=100, description="Max records to return"),
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    service = PatientService(db)
    return service.get_all_patients(skip=skip, limit=limit)

@router.get("/patients/{patient_id}", response_model=PatientResponse)
async def get_patient(patient_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    service = PatientService(db)
    return service.get_patient_by_id(patient_id)

@router.post("/patients", response_model=PatientResponse)
async def create_patient(patient_data: PatientCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    service = PatientService(db)
    return service.create_patient(patient_data)

@router.put("/patients/{patient_id}", response_model=PatientResponse)
async def update_patient(patient_id: int, patient_data: PatientUpdate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    service = PatientService(db)
    return service.update_patient(patient_id, patient_data)


@router.delete("/patients/{patient_id}", status_code=204)
async def delete_patient(patient_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    service = PatientService(db)
    service.delete_patient(patient_id)