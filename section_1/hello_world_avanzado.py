import logging
import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

 
load_dotenv()
 
logging.basicConfig(level=logging.INFO)
 
chat = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.7
)

platilla = PromptTemplate(
    input_variables=["nombre"],
    template="Saluda al usuario con su nombre. \nNombre del usuario: {nombre} \nAsistente:"
)

chain = platilla | chat

resultado = chain.invoke({"nombre": "Chris"})
print(resultado.content)



 
 