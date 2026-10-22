from sqlalchemy.orm import Session
from src.persistence.models import RecursoModel

class RecursoRepository:
    def obtener_todos(self, db: Session):
        return db.query(RecursoModel).all()