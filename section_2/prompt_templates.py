from langchain_core.prompts import PromptTemplate


template = "Eres un experto en marketing. Sugiere un slogan creativo para un producto {producto}"

prompt = PromptTemplate(
    template=template,
    input_variables=["producto"]
)

prompt_lleno = prompt.format(producto="Cafe organico")
print(prompt_lleno)