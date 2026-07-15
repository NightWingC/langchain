"""
Proyecto: CLI Chatbot
"""
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Configuracion
MODEL = "gpt-4o-mini"

SYSTEM_PROMPT = """Eres un asistente técnico experto en Python e IA.
Eres directo, usas ejemplos de código cuando es relevante,
y respondes en el mismo idioma que el usuario.
Si no sabes algo, lo dices honestamente."""

# Costos de la API en USD
INPUT_COST = 0.15
OUTPUT_COST = 0.60

class ChatBot:
    def __init__(self, system_prompt: str = SYSTEM_PROMPT):
        self.client = OpenAI()
        self.model = MODEL
        self.history: list[dict] = [
            {
                "role": "system",
                "content": system_prompt
            }
        ]
        self.total_tokens = 0
        self.total_cost = 0.0
        
    def chat(self, user_message: str) -> str:
        self.history.append({
            "role": "user",
            "content": user_message
        })
        
        response = self.client.chat.completions.create(
            model = self.model,
            messages = self.history,
            max_tokens = 1000,
            temperature = 0.7
        )  
        
        response_message = response.choices[0].message.content
        self.history.append({
            "role": "assistant",
            "content": response_message,
        })
        
        self._update_cost(response.usage)
        
        return response_message
    
    def _update_cost(self, usage) -> None:
        input_cost = (usage.prompt_tokens / 1_000_000) * INPUT_COST
        output_cost = (usage.completion_tokens / 1_000_000) * OUTPUT_COST
        self.total_tokens += usage.total_tokens
        self.total_cost += input_cost + output_cost
        
    def show_stats(self) -> None:
        print(f"'-" * 40)
        print("Sesión terminada")
        print(f"\nTotal tokens usados: {self.total_tokens}")
        print(f"\nTotal costo estimado: ${self.total_cost:.4f} USD")
        print(f"\n Turnos: {len(self.history) // 2}")
        print(f"'-" * 40)

def main():
    """Función principal"""
    print("╔══════════════════════════════════════╗")
    print("║      Python IA Aplicada - Chatbot    ║")
    print("║  Escribe 'quit' o Ctrl+C para salir  ║")
    print("╚══════════════════════════════════════╝\n")
    
    bot = ChatBot()
    
    try:
        while True:
            try:
                user_input = input("Tu: ").strip()
            except EOFError:
                break
            if not user_input:
                continue
            
            if user_input.lower() in ["quit", "exit", "salir", "bye"]:
                break 
            if user_input.lower() == "/stats":
                bot.show_stats()
                continue
            if user_input.lower() == "/reset":
                bot.history = [bot.history[0]]  
                print("Historial de conversación reiniciado.")
                continue
            
            print("\n AI: ", end="", flush=True)
            
            try: 
                response = bot.chat(user_input)
                print(response)
                print(f"\n Total tokens usados: {bot.total_tokens} | Costo estimado: ${bot.total_cost:.4f} USD \n" )
            except Exception as e:
                print("Error al procesar la solicitud:", e)
    except KeyboardInterrupt:
        print("\n")
    finally:
        bot.show_stats()
        print("¡Hasta luego!")


if __name__ == "__main__":
    main()