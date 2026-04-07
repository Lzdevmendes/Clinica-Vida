from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.services.doctor_service import DoctorService
from app.schemas.doctor_schema import DoctorResponse, DoctorCreate, DoctorUpdate
from app.routes.auth_routes import get_current_user

router = APIRouter()


@router.get("/doctors", response_model=List[DoctorResponse])
async def get_doctors(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    service = DoctorService(db)
    return service.get_all_doctors()


@router.get("/doctors/{doctor_id}", response_model=DoctorResponse)
async def get_doctor(doctor_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    service = DoctorService(db)
    return service.get_doctor_by_id(doctor_id)


@router.post("/doctors", response_model=DoctorResponse, status_code=201)
async def create_doctor(doctor_data: DoctorCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    service = DoctorService(db)
    return service.create_doctor(doctor_data)


@router.put("/doctors/{doctor_id}", response_model=DoctorResponse)
async def update_doctor(doctor_id: int, doctor_data: DoctorUpdate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    service = DoctorService(db)
    return service.update_doctor(doctor_id, doctor_data)


@router.delete("/doctors/{doctor_id}", status_code=204)
async def delete_doctor(doctor_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    service = DoctorService(db)
    service.delete_doctor(doctor_id)
