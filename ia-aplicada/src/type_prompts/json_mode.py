""""
JSON Mode
"""

import json
from src.helpers.ai_client import call_ai

def run_json_mode():
    # print("Texto libre")
    # print("=" *40)
    
    # response_text = call_ai([
    #     {"role": "user", "content": "Dame informacion sobre python: año de creación, creador y usos principales"}
    # ])
    
    # print(f"Respuest: \n {response_text}")
    
    print("\nJSON Mode:")
    print("=" *40)
    
    response_json = call_ai([
        {"role": "system", "content": "Responde siempre en formato JSON válido"},
        {"role": "user", "content": """Dame informacion sobre python en este formato exacto:
         {
            "language": "nombre",
            "creation_year": numero,
            "creator": "nombre",
            "principal_use":["uso1", "uso2", "uso3"]
         }
         
         """}
        
    ], 
        0.1, 
        "json_object"
    )
    
    json_data = json.loads(response_json)
    print("JSON:", json_data)
    print(f"Año de creacion: {json_data['creation_year']}")
    print(f"Creador: {json_data['creator']}")
    