from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal
from typing import Optional


class ConsultationBase(BaseModel):
    patient_id: int
    doctor_id: int
    start_datetime: datetime
    end_datetime: Optional[datetime] = None
    price: Optional[Decimal] = None
    consultation_type: Optional[str] = "regular"
    notes: Optional[str] = None


class ConsultationCreate(ConsultationBase):
    pass


class ConsultationUpdate(BaseModel):
    start_datetime: Optional[datetime] = None
    end_datetime: Optional[datetime] = None
    price: Optional[Decimal] = None
    status: Optional[str] = None
    consultation_type: Optional[str] = None
    notes: Optional[str] = None


class ConsultationResponse(ConsultationBase):
    id: int
    status: str
    created_at: datetime

    class Config:
        from_attributes = True
