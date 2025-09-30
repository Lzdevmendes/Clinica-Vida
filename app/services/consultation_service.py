from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from typing import List
from datetime import datetime
from app.models.consulta import Consultation
from app.schemas.consultation_schema import ConsultationCreate, ConsultationUpdate

class ConsultationService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_consultations(self) -> List[Consultation]:
        return self.db.query(Consultation).all()

    def get_consultation_by_id(self, consultation_id: int) -> Consultation:
        consultation = self.db.query(Consultation).filter(
            Consultation.id == consultation_id
        ).first()
        if not consultation:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Consultation not found"
            )
        return consultation

    def get_consultations_by_patient(self, patient_id: int) -> List[Consultation]:
        return self.db.query(Consultation).filter(
            Consultation.patient_id == patient_id
        ).all()

    def get_consultations_by_doctor(self, doctor_id: int) -> List[Consultation]:
        return self.db.query(Consultation).filter(
            Consultation.doctor_id == doctor_id
        ).all()

    def create_consultation(self, consultation_data: ConsultationCreate) -> Consultation:
        consultation = Consultation(**consultation_data.dict())
        self.db.add(consultation)
        self.db.commit()
        self.db.refresh(consultation)
        return consultation

    def update_consultation(self, consultation_id: int, consultation_data: ConsultationUpdate) -> Consultation:
        consultation = self.get_consultation_by_id(consultation_id)

        for field, value in consultation_data.dict(exclude_unset=True).items():
            setattr(consultation, field, value)

        self.db.commit()
        self.db.refresh(consultation)
        return consultation

    def update_consultation_status(self, consultation_id: int, new_status: str) -> Consultation:
        valid_statuses = ["pending", "confirmed", "cancelled", "completed"]
        if new_status not in valid_statuses:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid status. Must be one of: {', '.join(valid_statuses)}"
            )

        consultation = self.get_consultation_by_id(consultation_id)
        consultation.status = new_status
        self.db.commit()
        self.db.refresh(consultation)
        return consultation

    def delete_consultation(self, consultation_id: int) -> bool:
        consultation = self.get_consultation_by_id(consultation_id)
        self.db.delete(consultation)
        self.db.commit()
        return True