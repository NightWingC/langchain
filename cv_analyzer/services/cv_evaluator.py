import logging
import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from models.cv_model import AnalisisCV
from prompts.cv_prompts import crear_sistema_prompts
 
load_dotenv()
 
logging.basicConfig(level=logging.INFO)
 
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.2
)

def crear_evaluador_cv():
    modelo_base = llm
    modelo_estructurado = modelo_base.with_structured_output(AnalisisCV)
    chat_prompt = crear_sistema_prompts()
    cadena_evaluacion = chat_prompt | modelo_estructurado
    
    return cadena_evaluacion

def evaluar_candidato(texto_cv: str, descripcion_puesto: str) -> AnalisisCV:
    try:
        cadena_evaluacion = crear_evaluador_cv()
        resultado = cadena_evaluacion.invoke({
            "texto_cv": texto_cv,
            "descripcion_puesto": descripcion_puesto
        })
        
        return resultado
    except Exception as e:
        logging.error(f"Error al evaluar el CV: {e}")
        return AnalisisCV(
            nombre_candidato="Error al evaluar el CV",
            experiencia_anios=0,
            habilidades_clave=["Error al procesar el CV"],
            educacion="No se pudo evaluar la educación",
            experiencia_relevante="No se pudo evaluar la experiencia relevante",
            fortalezas=["No se pudieron evaluar las fortalezas"],
            areas_mejora=["No se pudieron evaluar las áreas de mejora"],
            porcentaje_ajuste=0
        )