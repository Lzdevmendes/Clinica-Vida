from sqlalchemy import Column, Integer, ForeignKey, Datetime, Numeric, String
from sqlalchemy.orm import relationship
from app.database import Base

class Consultation(Base):
  __tablename__ = "consultations"
  id = Column(Integer, primary_key=True, index=True)
  patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
  doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=False)
  start_datetime = Column(Datetime, nullable=False)
  price = Column(Numeric(10,2))
  status = Column(String, default="pending") # pending/accepted/refused/cancelled

patient = relationship("Patient")
doctor = relationship("Doctor")

