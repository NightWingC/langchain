from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "Eres un asistente util que mantiene el contexto de la conversación."),
    MessagesPlaceholder(variable_name="historial"),
    ("human", "Usuario:{pregunta_actual}"),
])

historial_conversacion = [
    HumanMessage(content="Usuario: Cual es la capital de Francia?"),
    AIMessage(content="AI: La capital de Francia es París."),
    HumanMessage(content="Usuario: ¿Cuál es la población de París?"),
    AIMessage(content="AI: La población de París es de aproximadamente 2.1 millones de habitantes."),
]

mensajes = chat_prompt.format_messages(
    historial= historial_conversacion,
    pregunta_actual="Puedes decirme algo interesante de su arquitectura"
)

for msg in mensajes:
    print(msg.content)