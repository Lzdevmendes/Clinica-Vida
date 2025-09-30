from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal
from typing import Optional

class ConsultationBase(BaseModel):
    patient_id: int
    doctor_id: int
    start_datetime: datetime
    price: Optional[Decimal] = None

class ConsultationCreate(ConsultationBase):
    pass

class ConsultationUpdate(BaseModel):
    start_datetime: Optional[datetime] = None
    price: Optional[Decimal] = None
    status: Optional[str] = None

class ConsultationResponse(ConsultationBase):
    id: int
    status: str

    class Config:
        from_attributes = True