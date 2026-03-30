import logging
import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
 
load_dotenv()
 
logging.basicConfig(level=logging.INFO)
 
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.7
)
 
ask = "¿Como fue la vida amorosa de la creadora de frankenstein, mary shelley?"
logging.info("Pregunta: " + ask)
 
response = llm.invoke(ask)
logging.info("Respuesta: " + response.content)