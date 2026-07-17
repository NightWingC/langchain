from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.rule import Rule
from rich.markdown import Markdown

from src.helpers.ai_client import call_ai

console = Console()

def create_code_analysis_prompt(
    code : str,
    language: str,
    detail_level: str = "medium"
) -> str:
    levels = {
        "basic": "Identifica solo bugs criticos",
        "medium": "Identifica bugs criticos, sugiere mejoras de rendimiento y legibilidad",
        "expert": "Analisis completo: bugs, seguridad, rendimiento, patrones de diseño"
    }
    
    return f"""
        Analizza el siguiente codigo: {language}
        Nivel de analisis requerio: {levels.get(detail_level, levels["medium"])}
        Lenguaje: {language}
        Codigo: {code}
    """
    
def run_prompt_templates():
    console.print(Rule("[bold yellow]Prompt Template"))
    example_code = """"
        def calcular_promedio(numeros):
            total=0
            for n in numeros:
                total = total+n
            return total/len(numeros)
    """
    
    syntax = Syntax(example_code, "python", theme="monokai", line_numbers=True)
    
    console.print(Panel(syntax, title="Codigo a analizar"))
    
    prompt = create_code_analysis_prompt(
        code=example_code,
        language="python",
        detail_level="expert"
    )
    
    response = call_ai([
        {"role": "user", "content": prompt}
    ])
    
    console.print(Panel(Markdown(response), title="Analisis del codigo",
                        border_style="green"))
    
    
