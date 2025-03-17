from fastapi import APIRouter, HTTPException, Depends
from models.patient_model import Patient
from modules.database import get_db
from sqlalchemy.orm import Session


router = APIRouter()

@router.post("/")
def create_patient(
    last_name: str,
    first_name: str,
    age: int,
    bmi: float,
    children: int,
    charge: float,
    email: str,
    sex_id: int,
    region_id: int,
    smoker_id: int,
    user_id: int,
    db: Session = Depends(get_db)
):
    

    new_patient = Patient(
        last_name=last_name,
        first_name=first_name,
        age=age,
        bmi=bmi,
        children=children,
        charge=charge,
        email=email,
        sex_id=sex_id,
        region_id=region_id,
        smoker_id=smoker_id,
        user_id=user_id
    )
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return new_patient

@router.get("/")
def read_patients(db: Session = Depends(get_db)):
    patients = db.query(Patient).all()
    return patients

@router.get("/{patient_id}")
def read_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = db.query(Patient).filter(Patient.user_id == patient_id).first()
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

@router.put("/{patient_id}")
def update_patient(
    patient_id: int,
    last_name: str,
    first_name: str,
    age: int,
    bmi: float,
    children: int,
    charge: float,
    email: str,
    sex_id: int,
    region_id: int,
    smoker_id: int,
    user_id: int,
    db: Session = Depends(get_db)
):
    patient = db.query(Patient).filter(Patient.user_id == patient_id).first()
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    patient.nom = last_name
    patient.prenom = first_name
    patient.age = age
    patient.bmi = bmi
    patient.children = children
    patient.charge = charge
    patient.email = email
    patient.region_id = region_id
    patient.sex_id = sex_id
    patient.smoker_id = smoker_id
    patient.user_id = user_id
    db.commit()
    db.refresh(patient)
    return patient

@router.delete("/{patient_id}")
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = db.query(Patient).filter(Patient.user_id == patient_id).first()
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    db.delete(patient)
    db.commit()
    return patient
