from pydantic import BaseModel, Field

class AnalisisCV(BaseModel):
    
    nombre_candidato: str = Field(description="Nombre completo del candidato extraido de cv")
    experiencia_anios: int = Field(description="Años de experiencia laboral del candidato relevante al puesto")
    habilidades_clave: list[str] = Field(description="Lista de las 5-7 del candidato mas relevantes al puesto")
    educacion: str = Field(description="Nivel educativo del candidato y especializacion principal")
    experiencia_relevante: str = Field(description="Resumen conciso de la experiencia laboral del candidato mas relevante al puesto")
    fortalezas: list[str] = Field(description="Lista de las 3-5 principales fortalezas del candidato")
    areas_mejora: list[str] = Field(description="Lista de las 3-5 areas donde el candidato podria mejorar")
    porcentaje_ajuste: int = Field(description="Porcentaje de ajuste del candidato al puest expericia, hablidad", ge=0, le=100)