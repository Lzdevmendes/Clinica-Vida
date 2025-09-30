from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel
from app.database import get_db
from app.services.consultation_service import ConsultationService
from app.schemas.consultation_schema import ConsultationResponse, ConsultationCreate, ConsultationUpdate
from app.routes.auth_routes import get_current_user

router = APIRouter()

class StatusUpdate(BaseModel):
    status: str

@router.get("/consultations", response_model=List[ConsultationResponse])
async def get_consultations(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    service = ConsultationService(db)
    return service.get_all_consultations()

@router.get("/consultations/{consultation_id}", response_model=ConsultationResponse)
async def get_consultation(consultation_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    service = ConsultationService(db)
    return service.get_consultation_by_id(consultation_id)

@router.post("/consultations", response_model=ConsultationResponse)
async def create_consultation(consultation_data: ConsultationCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    service = ConsultationService(db)
    return service.create_consultation(consultation_data)

@router.patch("/consultations/{consultation_id}/status", response_model=ConsultationResponse)
async def update_consultation_status(consultation_id: int, status_data: StatusUpdate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    service = ConsultationService(db)
    return service.update_consultation_status(consultation_id, status_data.status)

@router.put("/consultations/{consultation_id}", response_model=ConsultationResponse)
async def update_consultation(consultation_id: int, consultation_data: ConsultationUpdate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    service = ConsultationService(db)
    return service.update_consultation(consultation_id, consultation_data)