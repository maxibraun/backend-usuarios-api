from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuario"
    
    idusuario = Column(Integer, primary_key=True)
    nombre = Column(String)
    idpersona = Column(Integer)