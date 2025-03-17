from sqlalchemy import Column, Integer, String
from models.base import Base

class AppUser(Base):
    __tablename__ = "appuser"
    user_name = Column(String, primary_key=True, index=True)
    user_email = Column(String, nullable=False)
    user_password = Column(String, nullable=False)
    id_user = Column(Integer, unique=True, nullable=False)
    

