from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

plantilla_sistema = SystemMessagePromptTemplate.from_template("Eres un {rol} especializado en {especialidad}. Responde de manera {tono}")

plantilla_humano = HumanMessagePromptTemplate.from_template("Mi pregunta sobre {tema} es: {pregunta}")

chat_prompt = ChatPromptTemplate.from_messages([
    plantilla_sistema, 
    plantilla_humano,
])

mensajes = chat_prompt.format_messages(
    rol="nutricionista",
    especialidad="dietas veganas",
    tono="profesional y amigable",
    tema="Proteinas vegetales",
    pregunta="¿Cuál es la mejor dieta para obtener proteínas vegetales para un atleta?"
)

for msg in mensajes:
    print(msg.content)