from sqlalchemy import Column, Integer, String, ForeignKey, Float
from models.base import Base  

class Patient(Base):
    __tablename__ = "patient"

    user_id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, nullable=False)
    prenom = Column(String, nullable=False)
    age = Column(Integer, nullable=True)
    bmi = Column(Float, nullable=True)
    children = Column(Integer, nullable=True)
    charge = Column(Float, nullable=True)
    email = Column(String, nullable=True)

    # foreign key
    sex_id = Column(Integer, ForeignKey("sexe.id_sexe"), nullable=False)
    region_id = Column(Integer, ForeignKey("region.id_region"), nullable=False)
    smoker_id = Column(Integer, ForeignKey("smoker.id_smoker"), nullable=False)
    