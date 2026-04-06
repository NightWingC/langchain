from langchain_community.document_loaders import GoogleDriveLoader

credentials_path = "/langchain/client_secret_*.apps.googleusercontent.com.json"
token_path = "/langchain/token.json"

loader = GoogleDriveLoader(
    folder_id="1234567890abcdefg",  # Replace with your Google Drive folder ID
    credentials_path=credentials_path,
    token_path=token_path,
    recursive=True
)

documents = loader.load()
print(documents)
print(f"Metadata: {documents[0].metadata}")
print(f"Content: {documents[0].page_content}")
