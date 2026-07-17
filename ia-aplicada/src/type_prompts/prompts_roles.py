from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def show_roles():
    print("=" * 50)
    print("Roles: User (Sin rol system)")
    print("=" * 50)
    
    response_1 = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {
                "role": "user",
                "content": "¿Cuanto es 2 + 2?"
            }
        ]
    )
    
    print(f"Respuesta: {response_1.choices[0].message.content} \n")
    
    print("=" * 50)
    print("Rol: System")
    print("=" * 50)
    
    response_2 = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {
                "role": "system",
                "content": """ Eres un matematico gruñon que contesta preguntas simples con desden pero presicion absoluta. Siempre cincluyes un comentario basico que es la pregunta"""
            }, {
                "role": "user",
                "content": "¿Cuanto es 2 + 2?"
            }
        ]
    )
    
    print(f"Respuesta: {response_2.choices[0].message.content} \n")
    
    
    print("=" * 50)
    print("Rol: Assistant")
    print("=" * 50)
    
    response_3 = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {
                "role": "system",
                "content": """ Eres un clasificador de sentimientos. Respondes oslo con positivo, negativo o neutro.  """
            }, 
            { "role": "user", "content": "Me encanta el helado de mcdonalds" }, 
            { "role": "assistant", "content": "positivo" },
            { "role": "user", "content": "Odio lo lunes" }, 
            { "role": "assistant", "content": "negativo" },
            { "role": "user", "content": "El clima es templado" }, 
            { "role": "assistant", "content": "neutro" },
            { "role": "user", "content": "Odio los martes" }, 
        ]
    )
    
    print(f"Respuesta: {response_3.choices[0].message.content} \n")

if __name__ == "__main__":
    show_roles()
    
