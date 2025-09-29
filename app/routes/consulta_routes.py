from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.consulta import Consultation
from app.routes.auth_routes import get_current_user

router = APIRouter()

@router.get("/consultations")
async def get_consultations(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    consultations = db.query(Consultation).all()
    return consultations

@router.get("/consultations/{consultation_id}")
async def get_consultation(consultation_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    consultation = db.query(Consultation).filter(Consultation.id == consultation_id).first()
    if not consultation:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Consultation not found")
    return consultation

@router.patch("/consultations/{consultation_id}/status")
async def update_consultation_status(consultation_id: int, status: str, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    consultation = db.query(Consultation).filter(Consultation.id == consultation_id).first()
    if not consultation:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Consultation not found")

    consultation.status = status
    db.commit()
    db.refresh(consultation)
    return consultation