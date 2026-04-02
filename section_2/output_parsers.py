import logging
import os

from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
 
logging.basicConfig(level=logging.INFO)
 
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.6
)

class AnalisisTexto(BaseModel):
    resumen: str = Field(description="Un resumen breve del texto")
    sentimiento: str = Field(description="El sentimiento general del texto (positivo, negativo, neutral)")
    
structured_llm = llm.with_structured_output(AnalisisTexto)

texto_prueba = "Me encanta aprender sobre inteligencia artificial, pero a veces puede ser un poco abrumador."

resultado = structured_llm.invoke(f"Analiza el siguiente texto: {texto_prueba}")

print(resultado)
print(resultado.model_dump_json)
# print(dir(resultado))


    
