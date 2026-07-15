from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {   "role": "user",
            "content": "Traduce en tres idiomas: hello world" 
        }
    ]
)

text = response.choices[0].message.content
print(text)
print("\n -- Uso de tokens --")
print("Total tokens entrada: ", response.usage.prompt_tokens)
print("Total tokens salida: ", response.usage.completion_tokens)
print("Total tokens: ", response.usage.total_tokens)

cost_input = (response.usage.prompt_tokens / 1_000_000) * 0.15 #500 / 1_000_000 
cost_output = (response.usage.completion_tokens / 1_000_000) * 0.60 #500 / 1_000_000
cost_total = cost_input + cost_output

print("\n -- Costos estimados --")
print("Costo de entrada: $", cost_input)
print("Costo de salida: $", cost_output)
print("Costo total: $", cost_total)
print("\n ID de la respuesta generada: ", response.id)
print("Modelo utilizado: ", response.model)
