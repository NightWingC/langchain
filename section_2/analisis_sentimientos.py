import logging
import os
import json

from dotenv import load_dotenv
from langchain_core.runnables import RunnableLambda, RunnableParallel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate


load_dotenv()
 
logging.basicConfig(level=logging.INFO)
 
chat = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0,
    convert_system_message_to_human=True
)

def preprocess_text(text):
    """Limpia el texto eliminando espacios extras y limitando longitud"""
    return text.strip()[:500]

preprocess_text = RunnableLambda(preprocess_text)


def generate_summary(text):
    prompt = f"Resume en una sola oracion: {text}"
    response = chat.invoke(prompt)
    return response.content

summary_brach = RunnableLambda(generate_summary)

def analyze_sentiment(text):
    """Analiza el sentimiento y devuelve resultado estructurado"""
    prompt = f"""Analiza el sentimiento del siguiente texto.
    Responde ÚNICAMENTE en formato JSON válido:
    {{"sentimiento": "positivo|negativo|neutro", "razon": "justificación breve"}}
    
    Texto: {text}"""
    
    response = chat.invoke(prompt)
    try:
        return json.loads(response.content)
    except json.JSONDecodeError:
        return {"sentimiento": "neutro", "razon": "Error en análisis"}
    
sentiment_brach = RunnableLambda(analyze_sentiment)


def merge_results(data):
    """Combina los resultados de ambas ramas en un formato unificado"""
    return {
        "resumen": data["resumen"],
        "sentimiento": data["sentimiento_data"]["sentimiento"],
        "razon": data["sentimiento_data"]["razon"]
    }
    
merger = RunnableLambda(merge_results)

parralel_analysis = RunnableParallel({
    "resumen": summary_brach,
    "sentimiento_data": sentiment_brach
})
   
# Cadena completa
chain = preprocess_text | parralel_analysis | merger

review_batch = [
    "Excelente producto, superó mis expectativas.",
    "Terrible calidad, no lo recomiendo para nada.",
    "Esta bien, cumple su funcion basica pero nada especial."]
 
resultado_batch = chain.batch(review_batch)

print(resultado_batch)

