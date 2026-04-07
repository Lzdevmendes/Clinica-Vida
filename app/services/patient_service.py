from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.patient import Patient
from app.schemas.patient_schema import PatientCreate, PatientUpdate
from app.utils.exceptions import PatientNotFound, PatientProfileAlreadyExists

class PatientService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_patients(self, skip: int = 0, limit: int = 20) -> List[Patient]:
        return self.db.query(Patient).offset(skip).limit(limit).all()

    def get_patient_by_id(self, patient_id: int) -> Patient:
        patient = self.db.query(Patient).filter(Patient.id == patient_id).first()
        if not patient:
            raise PatientNotFound()
        return patient

    def get_patient_by_user_id(self, user_id: int) -> Optional[Patient]:
        return self.db.query(Patient).filter(Patient.user_id == user_id).first()

    def create_patient(self, patient_data: PatientCreate) -> Patient:
        existing_patient = self.get_patient_by_user_id(patient_data.user_id)
        if existing_patient:
            raise PatientProfileAlreadyExists()

        patient = Patient(**patient_data.dict())
        self.db.add(patient)
        self.db.commit()
        self.db.refresh(patient)
        return patient

    def update_patient(self, patient_id: int, patient_data: PatientUpdate) -> Patient:
        patient = self.get_patient_by_id(patient_id)

        for field, value in patient_data.dict(exclude_unset=True).items():
            setattr(patient, field, value)

        self.db.commit()
        self.db.refresh(patient)
        return patient

    def delete_patient(self, patient_id: int) -> bool:
        patient = self.get_patient_by_id(patient_id)
        self.db.delete(patient)
        self.db.commit()
        return True