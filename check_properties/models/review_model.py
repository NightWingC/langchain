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
    
    # observaciones: list[str] = Field(
    #     description="Lista de 3 o 5  observaciones relevantes identificadas durante la evaluación"
    # )
    
    # resumen_ejecutivo: str = Field(
    #     description="Resumen profesional y breve del estado general del inmueble para publicación"
    # )
    
    # puntaje_completitud_info_basica: int = Field(
    #     description="Puntaje de completitud de información básica (título, precio, ubicación, superficie)",
    #     ge=0,
    #     le=100,
    # )
    
    # puntaje_calidad_descripcion_presentacion: int = Field(
    #     description="Puntaje de calidad de redacción, claridad y presentación del anuncio",
    #     ge=0,
    #     le=100,
    # )
    
    # puntaje_aptitud_publicacion: int = Field(
    #     description="Puntaje general de aptitud para publicación en escala 0-100",
    #     ge=0,
    #     le=100,
    # )
    
    # puntaje_situacion_legal_documentacion: int = Field(
    #     description="Puntaje sobre situación legal y disponibilidad de documentación relevante",
    #     ge=0,
    #     le=100,
    # )
    
    # fortalezas: list[str] = Field(
    #     description="Lista de 3 a 6 fortalezas principales del inmueble para la publicación"
    # )
    
    # puntaje_coherencia_datos: int = Field(
    #     description="Puntaje de consistencia entre los datos técnicos y comerciales reportados",
    #     ge=0,
    #     le=100,
    # )

   
    