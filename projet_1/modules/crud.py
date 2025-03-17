from sqlalchemy.orm import Session
from models.patient_model import Patient
from models.region_model import Region
from models.sex_model import Sexe
from models.smoker_model import Smoker
# from models.appuser_model import AppUser

def create_patient(
    db: Session,
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
    user_id: int
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

def get_patient(db: Session, user_id: int):
    return db.query(Patient).filter(Patient.user_id == user_id).first()

def get_patients(db: Session):
    return db.query(Patient).all()

def update_patient(db: Session, patient_id: int, **kwargs):
    patient = get_patient(db, patient_id)
    if not patient:
        return None
    for key, value in kwargs.items():
        if value is not None:
            setattr(patient, key, value)
    db.commit()
    db.refresh(patient)
    return patient

def delete_patient(db: Session, patient_id: int):
    patient = get_patient(db, patient_id)
    if patient:
        db.delete(patient)
        db.commit()
        return patient
    return False

# CRUD operations for Region
def create_region(db: Session, region_name: str):
    new_region = Region(region_name=region_name)
    db.add(new_region)
    db.commit()
    db.refresh(new_region)
    return new_region

def get_region(db: Session, region_id: int):
    return db.query(Region).filter(Region.id_region == region_id).first()

def get_regions(db: Session):
    return db.query(Region).all()

def update_region(db: Session, region_id: int, region_name: str):
    region = get_region(db, region_id)
    if not region:
        return None
    region.region_name = region_name
    db.commit()
    db.refresh(region)
    return region

def delete_region(db: Session, region_id: int):
    region = get_region(db, region_id)
    if region:
        db.delete(region)
        db.commit()
        return region
    return False

# CRUD operations for Sex
def create_sex(db: Session, sex_type: str):
    new_sex = Sexe(sex_type=sex_type)
    db.add(new_sex)
    db.commit()
    db.refresh(new_sex)
    return new_sex

def get_sex(db: Session, sex_id: int):
    return db.query(Sexe).filter(Sexe.id_sex == sex_id).first()

def get_sexes(db: Session):
    return db.query(Sexe).all()

def update_sex(db: Session, sex_id: int, sex_type: str):
    sex = get_sex(db, sex_id)
    if not sex:
        return None
    sex.sex_type = sex_type
    db.commit()
    db.refresh(sex)
    return sex

def delete_sex(db: Session, sex_id: int):
    sex = get_sex(db, sex_id)
    if sex:
        db.delete(sex)
        db.commit()
        return sex
    return False

# CRUD operations for Smoker
def create_smoker(db: Session, smoking_status: str):
    new_smoker = Smoker(smoking_status=smoking_status)
    db.add(new_smoker)
    db.commit()
    db.refresh(new_smoker)
    return new_smoker

def get_smoker(db: Session, smoker_id: int):
    return db.query(Smoker).filter(Smoker.id_smoking_status == smoker_id).first()

def get_smokers(db: Session):
    return db.query(Smoker).all()

def update_smoker(db: Session, smoker_id: int, smoking_status: str):
    smoker = get_smoker(db, smoker_id)
    if not smoker:
        return None
    smoker.smoking_status = smoking_status
    db.commit()
    db.refresh(smoker)
    return smoker

def delete_smoker(db: Session, smoker_id: int):
    smoker = get_smoker(db, smoker_id)
    if smoker:
        db.delete(smoker)
        db.commit()
        return smoker
    return False

# # CRUD operations for AppUser
# def create_user_account(db: Session, user_name: str, user_email: str, user_password: str, id_user_type: int):
#     new_user_account = AppUser(
#         user_name=user_name,
#         user_email=user_email,
#         user_password=user_password,
#         id_user_type=id_user_type
#     )
#     db.add(new_user_account)
#     db.commit()
#     db.refresh(new_user_account)
#     return new_user_account

# def get_user_account(db: Session, user_account_id: int):
#     return db.query(AppUser).filter(AppUser.id_user_account == user_account_id).first()

# def get_user_accounts(db: Session):
#     return db.query(AppUser).all()

# def update_user_account(db: Session, user_account_id: int, user_name: str, user_email: str, user_password: str, id_user_type: int):
#     user_account = get_user_account(db, user_account_id)
#     if not user_account:
#         return None
#     user_account.user_name = user_name
#     user_account.user_email = user_email
#     user_account.user_password = user_password
#     user_account.id_user_type = id_user_type
#     db.commit()
#     db.refresh(user_account)
#     return user_account

# def delete_user_account(db: Session, user_account_id: int):
#     user_account = get_user_account(db, user_account_id)
#     if user_account:
#         db.delete(user_account)
#         db.commit()
#         return user_account
#     return False