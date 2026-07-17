""" Helper para crear y ejecutar el cliente de OpenAI """
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def call_ai(messages: list, temperature: float = 0.1, response_format: str = "text" ) -> str:
    """ Funcion que ejecuta el cliente """
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = messages,
        temperature = temperature,
        response_format = {"type": response_format}
    )
    return response.choices[0].message.content