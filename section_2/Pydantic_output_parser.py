import logging
import os

from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate


# 1. Modelo de datos
class AnalisisTexto(BaseModel):
    resumen: str = Field(description="Resumen breve del texto")
    sentimiento: str = Field(description="Sentimiento: Positivo, Neutro o Negativo")
    palabras_clave: list[str] = Field(description="3-5 palabras clave principales")

# 2. Parser
parser = PydanticOutputParser(pydantic_object=AnalisisTexto)

# 3. Prompt
prompt = PromptTemplate(
    template="""Analiza este texto cuidadosamente y proporciona un análisis estructurado:
 
{format_instructions}
 
TEXTO:
{texto}
 
ANÁLISIS:""",
    input_variables=["texto"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

load_dotenv()
 
logging.basicConfig(level=logging.INFO)
 
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0,
    convert_system_message_to_human=True
)

# 5. Cadena
chain = prompt | llm | parser
 
# 6. Ejecución
if __name__ == "__main__":
    texto = "Me encantó la nueva película de acción, tiene efectos especiales increíbles."
    
    try:
        resultado = chain.invoke({"texto": texto})
        print("✅ Análisis exitoso:")
        print(resultado.model_dump_json(indent=2))
    except Exception as e:
        print(f"❌ Error: {e}")