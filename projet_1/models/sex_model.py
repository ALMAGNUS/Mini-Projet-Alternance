from sqlalchemy import Column, Integer, String
from models.base import Base  

class Sexe(Base):
    __tablename__ = "sexe"
    id_sexe = Column(Integer, primary_key=True, index=True)
    sex_label = Column(String, nullable=False)
    