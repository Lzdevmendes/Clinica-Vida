from pydantic import BaseModel
from datetime import date
from typing import Optional

class PatientBase(BaseModel):
    name: str
    birth_date: Optional[date] = None
    phone: Optional[str] = None
    address: Optional[str] = None

class PatientCreate(PatientBase):
    user_id: int

class PatientUpdate(BaseModel):
    name: Optional[str] = None
    birth_date: Optional[date] = None
    phone: Optional[str] = None
    address: Optional[str] = None

class PatientResponse(PatientBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True