import os
from dotenv import load_dotenv
from google.genai import Client

load_dotenv()

# Crear cliente
client = Client(api_key=os.getenv("GOOGLE_API_KEY"))

# Listar modelos disponibles
print("Modelos disponibles:")
for model in client.models.list():
    print(f"- {model.name}")
    if "embed" in model.name.lower():
        print(f"  ✓ Soporta embedding")
