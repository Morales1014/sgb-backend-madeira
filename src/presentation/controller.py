from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.logic.service import RecursoService

router = APIRouter(prefix="/api/recursos", tags=["Recursos"])
service = RecursoService()

@router.get("")
def get_recursos(db: Session = Depends(get_db)):
    recursos = service.listar_recursos_estructurados(db)
    return {"exito": True, "data": recursos}