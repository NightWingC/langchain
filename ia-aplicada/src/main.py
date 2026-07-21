from rich.console import Console
from rich.panel import Panel

from src.type_prompts.zero_few_shot import run_zero_shot
from src.type_prompts.cot_prompts import run_chain_of_thought
from src.type_prompts.prompt_template import run_prompt_templates
from src.type_prompts.json_mode import run_json_mode
from src.type_prompts.news_extractor import run_news_extractor
from src.type_prompts.news_extractor import run_news_extractor
from src.type_prompts.function_calling import run_chat_with_tools 



console = Console()

def main():
    console.print(
        Panel.fit(
            "[bold cyan]Técnica de prompting\n"
        )
    )
    
    # run_zero_shot()
    # run_chain_of_thought()
    # run_prompt_templates()
    # run_json_mode()
    # run_news_extractor()
    run_chat_with_tools("Que clima hace en madrid?")
    run_chat_with_tools("Que clima hace en mexico city?")
    run_chat_with_tools("Que clima hace en London?")
    run_chat_with_tools("Que clima hace en Buenos Aires?")
    run_chat_with_tools("Que clima hace en Tampico?")

    
    
    console.print("\n[bold green]Ejecución completada\n")
    
if __name__ == "__main__":
    main()
    