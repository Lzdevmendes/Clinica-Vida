from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Doctor(Base):
    __tablename__ = "doctors"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String, nullable=False)
    specialty = Column(String)
    license_number = Column(String, unique=True, nullable=False)
    phone = Column(String)

    user = relationship("User")
    consultations = relationship("Consultation", back_populates="doctor")