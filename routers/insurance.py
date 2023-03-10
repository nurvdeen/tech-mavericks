#!/usr/bin/python3

"""End point routes for insurance company"""

from dependencies.depends import get_current_user
from fastapi import APIRouter, Depends, status, HTTPException
from schema.insurance import ShowInsurance
from fastapi import APIRouter, Depends,status, HTTPException
from schema import insurance as insuranceSchema
from engine.loadb import load
from models import insurance as insuranceModel
from sqlalchemy.orm import Session
from typing import Dict, List
from utils.acl import check_role
from utils import auth


router = APIRouter(
    prefix="/insurance",
    tags=["insurance"]
)


@router.post("/admin/register", response_model=insuranceSchema.ShowInsurance, status_code=status.HTTP_201_CREATED)
def create_in_admin(request: insuranceSchema.InAdmin, db: Session = Depends(load)):
    phone = request.phone
    insuranceID = request.insuranceID

    checkPhone = db.query_eng(insuranceModel.InAdmin).filter(
        insuranceModel.InAdmin.phone == phone).first()
    checkInsuranceID = db.query_eng(insuranceModel.InAdmin).filter(
        insuranceModel.InAdmin.insuranceID == insuranceID).first()

    if checkPhone:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"Insurance admin with phone: {phone} exists")
    if checkInsuranceID:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"Insurance admin with Insurance ID: {insuranceID} exists")

    passwd_hash = auth.get_password_hash(request.password2.get_secret_value())

    new_inAdmin = insuranceModel.InAdmin(
        name=request.name, phone=request.phone, email=request.email, password_hash=passwd_hash, insuranceID=request.insuranceID)
    db.new(new_inAdmin)
    db.save()
    return new_inAdmin


@router.get("/admin/all", response_model=List[insuranceSchema.ShowInsurance], status_code=status.HTTP_200_OK)
def all_admins(db: Session = Depends(load), user_data: get_current_user = Depends()):
    check_role('insurance_admin', user_data['user_id'])
    admins = db.query_eng(insuranceModel.InAdmin).all()
    return admins


@router.get("/admin/insuranceID/{insuranceID}", response_model=insuranceSchema.ShowInsurance, status_code=status.HTTP_200_OK)
def show_admin(insuranceID, db: Session = Depends(load), user_data: get_current_user = Depends()):
    check_role('insurance_admin', user_data['user_id'])
    admin = db.query_eng(insuranceModel.InAdmin).filter(
        insuranceModel.InAdmin.insuranceID == insuranceID).first()
    if not admin:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"admin with the insurance ID: {insuranceID} not found")
    return admin


@router.post("/register", response_model=insuranceSchema.ShowInsurance, status_code=status.HTTP_201_CREATED)
def create_insurance(request: insuranceSchema.Insurance, db: Session = Depends(load), user_data: get_current_user = Depends()):
    check_role('insurance_admin', user_data['user_id'])
    phone = request.phone
    insuranceID = request.insuranceID
    checkPhone = db.query_eng(insuranceModel.Insurance).filter(
        insuranceModel.Insurance.phone == phone).first()
    checkInsuranceID = db.query_eng(insuranceModel.Insurance).filter(
        insuranceModel.Insurance.insuranceID == insuranceID).first()

    if checkPhone:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"insurance with phone: {phone} exists")
    if checkInsuranceID:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"insurance with insurance ID: {insuranceID} exists")

    new_insurance = insuranceModel.Insurance(
        name=request.name, phone=request.phone, insuranceID=request.insuranceID, address=request.address)
    db.new(new_insurance)
    db.save()
    return new_insurance


@router.get("/all", response_model=List[insuranceSchema.ShowInsurance], status_code=status.HTTP_200_OK)
def all(db: Session = Depends(load), user_data: get_current_user = Depends()):
    check_role('insurance_admin', user_data['user_id'])
    companies = db.query_eng(insuranceModel.Insurance).all()
    return companies


@router.get("/{insuranceID}", response_model=insuranceSchema.ShowInsurance, status_code=status.HTTP_200_OK)
def show(insuranceID, db: Session = Depends(load), user_data: get_current_user = Depends()):
    check_role('insurance_admin', user_data['user_id'])
    company = db.query_eng(insuranceModel.Insurance).filter(
        insuranceModel.Insurance.insuranceID == insuranceID).first()
    if not company:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"company with the insurance ID: {insuranceID} not found")
    return company

