import json
import os
from dotenv import load_dotenv
from src.helpers.ai_client import call_ai
from src.services.news_service import NewsService

load_dotenv()

def run_news_extractor():
    print("Extractor de noticias")
    print("=" * 40)
    
    # news = """
    # Apple anunció hoy que Tim Cook presentará el nuevo iPhone 17 Pro
    # el próximo 15 de septiembre de 2025 en Cupertino, California.
    # El dispositivo costará desde $1,199 USD y contará con chip A19.
    # """
    
    news_services = NewsService(os.getenv("NEWS_API_KEY"))
    news = news_services.get_latests_tech_news()
    
    response_extractor = call_ai([
        {"role": "system", "content": """
            Eres un extractor de informacion de noticias. Si la noticia esta enotro idioma, traduce al español.
            
            Extrae entidades y devueve solo JSON valido con esta estrutura: 
            
            {
                "company": string,
                "person": string,
                "product": string,
                "top_news": string,
                "keywords": string,
                "date_time": string(format ISO: YYYY-MM-DD ),
                "place": string,
                "price": number or null
            }
         """}, 
        { "role": "user", "content": news }
    ], 
        0.1,
        "json_object"
    )
    
    extract_entities = json.loads(response_extractor) 
    for key,  value in extract_entities.items():
        print(f"{key}: {value}")