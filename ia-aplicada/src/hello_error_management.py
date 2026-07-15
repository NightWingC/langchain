2

load_dotenv()

def call_ai(question: str) -> str:
    client = OpenAI()
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                { 
                    "role": "user",
                    "content": question 
                }
            ], 
            max_tokens=500,
            temperature=0.7 #0=determinista, 1=creativo, 2=muy creativo
        )
        return response.choices[0].message.content
    
    except AuthenticationError:
        print("API KEY invalido. Revisa tu archivo .env y asegúrate de que la variable OPENAI_API_KEY esté correctamente configurada.")
        raise SystemExit(1)
    
    except RateLimitError:
        print("Limite de velocidad alcanzado. Espera un momento.")
        raise SystemExit(1)
    
    except APIConnectionError:
        print("Sin conexión con la API. Verifica tu conexión a internet.")
        raise SystemExit(1)
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {type(e).__name__}: {e}")
        raise SystemExit(1)
    
if __name__ == "__main__":
    response = call_ai("¿Cuál es la capital de México?")
    print(f"IA: {response}")
