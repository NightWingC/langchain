import json
from src.helpers.ai_client import call_ai_tools
from src.services.weather_service import WeatherService

TOOLS = [
    { 
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Obtine el clima actual de una ciudad. Usar cuando el usuario pregunta por el clima",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "El numbre de la ciudad, ej: 'Madrid' o 'Mexico city'"
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": "Unidad de temperatura"
                    }
                },
                "required": ["city"]
            }
        }
    }
]

def get_weather(city: str, unit: str = "celsius") -> dict:
    """Obtener clima"""

    # simulated_data = {
    #     "madrid": {"temperature": 18, "wind_speed": 10.2},
    #     "mexico city": {"temperature": 22, "wind_speed": 1.0},
    #     "london": {"temperature": 12, "wind_speed": 2.0},
    # }
    
    # city_lower = city.lower
    # weather_data = simulated_data.get(
    #     city_lower,
    #     { "temperature": 20, "wind_speed": 1.0 }
    # )
    
    weather_service = WeatherService()
    weather = weather_service.get_current_weather_by_city(city)
    print(weather["temperature"])
    
    temp = weather["temperature"]
    if unit == "fahrenheit":
        temp = (temp * 9/5) + 32
        
    return {
        "city": city,
        "temperature": f"{temp} {'C' if unit == 'celsius' else 'F'}",
        "wind_speed": f"{weather.get('windspeed', 0)} km/h"
    }
    
def execute_tool(name: str, arguments: dict) -> str:
    available_functions = {
        "get_weather": get_weather,
    }
    
    if name not in available_functions:
        return json.dumps({ "error:" f"Funcion {name} no encontrada"})
    
    result = available_functions[name](**arguments)
    
    return json.dumps(result, ensure_ascii=False)

def run_chat_with_tools(user_message: str) -> str:
    messages = [
        {
            "role": "system",
            "content": "Eres un asistente útil con acceso a herramientas.",
        }, {
            "role": "user",
            "content": user_message
        }
    ]
    
    print(f"\nUsuario: {user_message}")
    message_ia = call_ai_tools(messages, 0.1, "text", TOOLS, "auto")
    
    if message_ia.tool_calls:
        print(f"AI decide usar herramientas")
        messages.append(message_ia)
        
        for tool_call in message_ia.tool_calls:
            function_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)
            
            print(f"{function_name}({arguments})")
            
            result = execute_tool(function_name, arguments)
            print(f"Resultado: {result}")
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": result
            })
            
        final_response = call_ai_tools(messages, 0.1, "text", TOOLS)
    else: 
        final_response = message_ia
    
    print(f"AI: {final_response.content}")
    return final_response.content
    
    