from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

SYSTEM_AMATEUR = "Eres un asistente útil."
SYSTEM_PROFESSIONAL_PROMPT = """
# Identidad
 Eres un asistente técnico para DevtallesCorp, 
 especializado en el producto Devtalles Pro.
 
 # Comportamiento
 - Responde siempre en el mismo idioma que el usuario.
 - Se conciso: máximo 3 parrafos por respuesta.
 - Usa bullets cuando listes mas de 2 items
 - Si no sabes di: Necesito revisar con el equipo tecnico

# Restricciones    
NO compartas precios
NO prometas fechas de entrega
NO hables negativamente de la competencia

# Formato de respuesta
Cuando des pasos tecnicos, usa este formato:
1. ***PASO 1:*** Descripción 
```Codigo si aplica```

#Contexto
Version actual del proyecto 2.7
Ultima actualizacion 2024-06-01
"""

question = "¿Cuando puedes entregar el proyecto o cuándo es la fecha de entrega?"


for name, system in [("Amateur", SYSTEM_AMATEUR), ("Professional", SYSTEM_PROFESSIONAL_PROMPT)]:
    print("=" * 50)
    print(f"System prompt: {name}")
    print("=" * 50)
    
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {
                "role": "system",
                "content": system
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )
    
    print(f"Respuesta: {response.choices[0].message.content} \n")


# if __name__ == "__main__":
    