from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.sex_model import Sexe
from modules.database import get_db

router = APIRouter()

@router.post("/")
def create_sex(sex_type: str, db: Session = Depends(get_db)):
    new_sex = Sexe(sex_type=sex_type)
    db.add(new_sex)
    db.commit()
    db.refresh(new_sex)
    return new_sex

@router.get("/")
def read_sexes(db: Session = Depends(get_db)):
    sexes = db.query(Sexe).all()
    return sexes

@router.get("/{sex_id}")
def read_sex(sex_id: int, db: Session = Depends(get_db)):
    sex = db.query(Sexe).filter(Sexe.id_sex == sex_id).first()
    if sex is None:
        raise HTTPException(status_code=404, detail="Sex not found")
    return sex

@router.put("/{sex_id}")
def update_sex(sex_id: int, sex_type: str, db: Session = Depends(get_db)):
    sex = db.query(Sexe).filter(Sexe.id_sex == sex_id).first()
    if sex is None:
        raise HTTPException(status_code=404, detail="Sex not found")
    sex.sex_type = sex_type
    db.commit()
    db.refresh(sex)
    return sex

@router.delete("/{sex_id}")
def delete_sex(sex_id: int, db: Session = Depends(get_db)):
    sex = db.query(Sexe).filter(Sexe.id_sex == sex_id).first()
    if sex is None:
        raise HTTPException(status_code=404, detail="Sex not found")
    db.delete(sex)
    db.commit()
    return sex