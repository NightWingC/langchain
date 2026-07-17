from rich.console import Console
from rich.table import Table
from rich.rule import Rule

from src.helpers.ai_client import call_ai

console = Console()

def run_zero_shot():
    console.print(Rule("[bold yellow]Técnica Zero-Shot and Few-Shot[/bold yellow]"))
    zero_shot = call_ai([
        {
            "role": "user",
            "content": "Clasifica este email como urgente o normal"
            "'El servide de produccion esta caido, los clientes no pueden acceder'"
        }
    ])
    
    few_shot = call_ai([
        {
            "role": "system",
            "content": "Clasifica email. Responde solo con: Urgente o Normal. Sin explicación"
        },
        {
            "role": "user",
            "content": "Tengo una reunion mañana"
        },
        {
            "role": "assistant",
            "content": "NORMAL"
        },
        {
            "role": "user",
            "content": "La base de datos esta caida en producción"
        },
        {
            "role": "assistant",
            "content": "URGENTE"
        },
        {
            "role": "user",
            "content": "Puedes revisar mi PR cuando tengas oportunida"
        },
        {
            "role": "assistant",
            "content": "NORMAL"
        },
        {
            "role": "user",
            "content": "El servidor esta caído y los clientes tienen problemas"
        },
        {
            "role": "user",
            "content": "Agendar una actividad recreativa"
        },
    ])
    
    table = Table(title="Comparacion")
    table.add_column("Técnica", style="cyan")
    table.add_column("Resultado", style="magenta")
    
    table.add_row("Zero-shot", zero_shot)
    table.add_row("Few-shot", few_shot)
    
    console.print(table)
    