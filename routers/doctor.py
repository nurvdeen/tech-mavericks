from fastapi import APIRouter, Depends, status, HTTPException
from schema import doctor as doctorSchema
from engine.loadb import load
from models import doctor as doctorModel
from models import user as userModel
from sqlalchemy.orm import Session
from typing import Dict, List
from utils import auth

router = APIRouter(
    prefix="/doctor",
    tags=["doctor"]
)


@router.post("/register", response_model=doctorSchema.ShowDoctor,
             status_code=status.HTTP_201_CREATED)
def create_doctor(request: doctorSchema.Doctor, db: Session = Depends(load)):
    phone = request.phone
    email = request.email

    checkPhone = db.query_eng(userModel.Users).filter(
        userModel.Users.phone == phone).first()
    checkEmail = db.query_eng(userModel.Users).filter(
        userModel.Users.email == email).first()
    if checkPhone:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"user with phone: {phone} exists")
    if checkEmail:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"user with email: {email} exists")

    passwd_hash = auth.get_password_hash(request.password2.get_secret_value())

    new_doctor = doctorModel.Doctor(name=request.name, phone=request.phone,
                                    email=request.email, address=request.address, password_hash=passwd_hash,
                                    insuranceID=request.hospitalID, dob=request.dob, gender=request.gender)
    db.new(new_doctor)
    db.save()
    return new_doctor


@router.get("/all", response_model=List[doctorSchema.ShowDoctor], status_code=status.HTTP_200_OK)
def all(db: Session = Depends(load)):
    doctor = db.query_eng(doctorModel.Doctor).all()
    return doctor


@router.get("/email/{email}", response_model=doctorSchema.ShowDoctor, status_code=status.HTTP_200_OK)
def show(email, db: Session = Depends(load)):
    doctor = db.query_eng(doctorModel.Doctor).filter(
        doctorModel.Doctor.email == email).first()
    if not doctor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"doctor with the email {email} not found")
    return doctor