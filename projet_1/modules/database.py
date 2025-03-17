import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
                
from models.base import Base, engine, SessionLocal


from models.sex_model import Sexe
from models.patient_model import Patient
from models.smoker_model import Smoker
from models.region_model import Region
from models.appuser_model import AppUser


def init_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

init_db()