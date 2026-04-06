from langchain_community.document_loaders import PyPDFLoader, WebBaseLoader

loader = PyPDFLoader("cv.pdf")

pages = loader.load()
for i, page in enumerate(pages):
    print(f"=== Pagina {i+1} ===")
    print(f"Contenido: {page.page_content}")
    print(f"Metadatos: {page.metadata}")
    
loaderWeb = WebBaseLoader("https://techmind.ac/")

docsWeb = loaderWeb.load()
print(docsWeb)
