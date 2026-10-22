from sqlalchemy import Column, Integer, String
from src.config.database import Base

class RecursoModel(Base):
    __tablename__ = "recursos"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    isbn = Column(String, nullable=False)
    coleccion = Column(String, nullable=False)
    estado = Column(String, default="Disponible")