from sqlalchemy import Column, Integer, String
from database import Base

class Usuario(Base):
    __tablename__ = "usuario"

    idusuario = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    idpersona = Column(Integer)
    password = Column(String, nullable=False)