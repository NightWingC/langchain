from langchain_community.document_loaders import PyPDFLoader
from mll.mll import mll
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Cargar el documento PDF
loader = PyPDFLoader("docs/quijote.pdf")
pages = loader.load()

# Dividir el texto en chunks mas pequeños
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=3000, 
    chunk_overlap=200
)

chunks = text_splitter.split_documents(pages)

# Combinar todas las pagainas en un texto único
full_text = ""
for page in pages:
    full_text += page.page_content + "\n"
  
#Pasar el texto al LLM 
summaries = []
for chunk in chunks:
    response = mll.invoke(f"HAz un resumen de los puntos mas importantes del siguiente texto: {chunk.page_content}")
    summaries.append(response. content)

final_summary = mll.invoke(f"Combina y sintetiza estos resumenes en un resumen coherente y completo: {" ".join(summaries)}")
print(final_summary.content)

