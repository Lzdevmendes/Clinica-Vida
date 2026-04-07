from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.doctor import Doctor
from app.schemas.doctor_schema import DoctorCreate, DoctorUpdate
from app.utils.exceptions import DoctorNotFound, LicenseAlreadyRegistered


class DoctorService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_doctors(self) -> List[Doctor]:
        return self.db.query(Doctor).all()

    def get_doctor_by_id(self, doctor_id: int) -> Doctor:
        doctor = self.db.query(Doctor).filter(Doctor.id == doctor_id).first()
        if not doctor:
            raise DoctorNotFound()
        return doctor

    def get_doctor_by_license(self, license_number: str) -> Optional[Doctor]:
        return self.db.query(Doctor).filter(Doctor.license_number == license_number).first()

    def create_doctor(self, doctor_data: DoctorCreate) -> Doctor:
        if self.get_doctor_by_license(doctor_data.license_number):
            raise LicenseAlreadyRegistered()

        doctor = Doctor(**doctor_data.dict())
        self.db.add(doctor)
        self.db.commit()
        self.db.refresh(doctor)
        return doctor

    def update_doctor(self, doctor_id: int, doctor_data: DoctorUpdate) -> Doctor:
        doctor = self.get_doctor_by_id(doctor_id)

        for field, value in doctor_data.dict(exclude_unset=True).items():
            setattr(doctor, field, value)

        self.db.commit()
        self.db.refresh(doctor)
        return doctor

    def delete_doctor(self, doctor_id: int) -> bool:
        doctor = self.get_doctor_by_id(doctor_id)
        self.db.delete(doctor)
        self.db.commit()
        return True
