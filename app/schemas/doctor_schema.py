from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class DoctorBase(BaseModel):
    name: str
    specialty: Optional[str] = None
    license_number: str
    phone: Optional[str] = None


class DoctorCreate(DoctorBase):
    user_id: int


class DoctorUpdate(BaseModel):
    name: Optional[str] = None
    specialty: Optional[str] = None
    phone: Optional[str] = None


class DoctorResponse(DoctorBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True
