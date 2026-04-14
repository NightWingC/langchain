from typing import Literal
from pydantic import BaseModel, Field

class ReviewModel(BaseModel):
    
    datos_faltantes: list[str] = Field(
        description="Campos o datos faltantes que se deben completar antes de publicar"
    )
    inconsistencias_detectadas: list[str] = Field(
        description="Lista de 1 - 5 inconsistencias o contradicciones detectadas en la información"
    )
    recomendacion: str= Field(
        description="Recomendacion de acciones concretas para mejorar el anuncio y facilitar su publicación"
    )
    
    veredicto_publicacion: Literal["APROBADO", "RECHAZADO"] = Field(
        description="Resultado final sobre la publicación del inmueble"
    )
    
class ReviewPropertyResponse(BaseModel):
	status: str
	mensaje: str

   
    