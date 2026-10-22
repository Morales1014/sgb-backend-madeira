from sqlalchemy.orm import Session
from src.persistence.repository import RecursoRepository

class RecursoService:
    def __init__(self):
        self.repository = RecursoRepository()

    def listar_recursos_estructurados(self, db: Session):
        recursos = self.repository.obtener_todos(db)
        resultado = []
        for r in recursos:
            dias_max = 15 if r.coleccion == "General" else 5
            renovaciones_max = 5 if r.coleccion == "General" else 0
            resultado.append({
                "id": r.id,
                "titulo": r.titulo,
                "isbn": r.isbn,
                "coleccion": r.coleccion,
                "estado": r.estado,
                "diasPrestamoMax": dias_max,
                "renovacionesMax": renovaciones_max
            })
        return resultado