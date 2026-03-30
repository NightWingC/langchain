import logging
import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.prompts import PromptTemplate
import streamlit as st 

load_dotenv()
 
logging.basicConfig(level=logging.INFO)

#Configurar la pagina de la app
st.set_page_config(
    page_title="Chatbot Basico",
    page_icon=":robot_face:",
)
st.title("Chatbot basico con langchain y Google Gemini")
st.markdown("Este es un chatbot de ejemplo* construido con Streamlit + Langchain. Escribe tu mensaje.")

with st.sidebar:
    st.header("Configuración")
    temperature = st.slider("Temperatura", 0.0, 1.0, 0.5, 0.1)
    model_name = st.selectbox("Modelo", ["gemini-2.5-flash", "gemini-1.5-pro", "gemini-1.5-flash"])

    # Recrea el modelo cada vez que se cambie la configuración
    chat_model = ChatGoogleGenerativeAI(model=model_name, temperature=temperature)

# Inicializar el historial de mensajes
if "mensajes" not in st.session_state:
    st.session_state.mensajes = []
    
#Crear el template de prompt con comportamiento especifico
prompt_template = PromptTemplate(
    input_variables=["mensaje", "historial"],
    template="""Eres un asistente util y amigable llamdo Chatbot PRO.
    
    Historila de conversacion:
    {historial}
    
    Responde de manera clara y concisa a las siguiente pregunta: {mensaje}
    """
)

# Crear cadena usando LCEL(LangChian Expression Language)
cadena = prompt_template | chat_model
    
# Mostrar mensajes previos en la interfaz
for msg in st.session_state.mensajes:
    if isinstance(msg, SystemMessage):
        #No muestro el mensaje por pantalla
        continue
    
    role = "assistant" if isinstance(msg, AIMessage) else "user"
    with st.chat_message(role):
        st.markdown(msg.content)
        

 # input de entrada de texto de usuario 
pregunta = st.chat_input("Escribe tu mensaje: ")
 
if pregunta:
    # Mostrar inmediatamente el mensaje del usuario en la interface
    with st.chat_message("user"):
        st.markdown(pregunta)
        
    # Almacenamos el mensaje en la memoria de streamlit
    st.session_state.mensajes.append(HumanMessage(content=pregunta))
    
    #Generar respuesta usando el modelo del lenguaje
    respuesta = chat_model.invoke(st.session_state.mensajes)

    #Mostrar la respuesta por interface
    with st.chat_message("assistant"):
        st.markdown(respuesta.content)
        
    st.session_state.mensajes.append(respuesta)
    
    
     





