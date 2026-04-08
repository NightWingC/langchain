from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv 

load_dotenv()

vectorstores = Chroma(
    embedding_function=GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001"),
    persist_directory="../chroma_db",
)

retriever = vectorstores.as_retriever(search_type="similarity", search_kwargs={"k": 2})

consulta = "Donde se encuentra el local de contrato en el que participa Maria Jimenez Campos?"

resultados = retriever.invoke(consulta)

print("Top 2 resultados para la consulta: \n")
for i, doc in enumerate(resultados, start=1):
    print(f"Resultado {i}")
    print(f"Contenido: {doc.page_content}")
    print(f"Metadatos: {doc.metadata}\n")
