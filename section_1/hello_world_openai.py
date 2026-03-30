import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
	raise ValueError("Falta OPENAI_API_KEY en el archivo .env")

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

pregunta = "¿En que año llego el hombre a la luna?"
print("pregunta: ", pregunta)

respuesta = llm.invoke(pregunta)
print("respuesta: ", respuesta.content)