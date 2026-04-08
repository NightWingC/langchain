from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
from dotenv import load_dotenv 

load_dotenv()

loader = PyPDFDirectoryLoader("docs/contratos")
documentos = loader.load()

print(f"Documentos cargados: {len(documentos)} documentos desde el directorio 'docs/contratos'")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, 
    chunk_overlap=200
)

docs_split = text_splitter.split_documents(documentos)
print(f"Se crearon {len(docs_split)} fragmentos de texto.")

vectorstores = Chroma.from_documents(
    docs_split,
    embedding=GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001"),
    persist_directory="./chroma_db",
    collection_name="contratos",
)

consulta = "Donde se encuentra el local de contrato en el que participa Maria Jimenez Campos"

resultados = vectorstores.similarity_search(consulta, k=2)
print("Top 3 resultados para la consulta: \n")
for i, doc in enumerate(resultados, start=1):
    print(f"Resultado {i}")
    print(f"Contenido: {doc.page_content}")
    print(f"Metadatos: {doc.metadata}\n")
