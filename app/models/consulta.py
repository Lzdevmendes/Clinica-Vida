from sqlalchemy import Column, Integer, ForeignKey, DateTime, Numeric, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Consultation(Base):
  __tablename__ = "consultations"
  id = Column(Integer, primary_key=True, index=True)
  patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
  doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=False)
  start_datetime = Column(DateTime, nullable=False)
  end_datetime = Column(DateTime)
  price = Column(Numeric(10,2))
  status = Column(String, default="pending")
  notes = Column(Text)
  consultation_type = Column(String, default="regular")
  created_at = Column(DateTime(timezone=True), server_default=func.now())
  updated_at = Column(DateTime(timezone=True), onupdate=func.now())

  patient = relationship("Patient", back_populates="consultations")
  doctor = relationship("Doctor", back_populates="consultations")

