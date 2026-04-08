# Configuración de modelos
EMBEDDING_MODEL = "models/gemini-embedding-001"
QUERY_MODEL = "models/gemini-2.5-flash-lite"
GENERATION_MODEL = "models/gemini-flash-latest"

# Configuración de vector store
CHROMA_DB_PATH = "../chroma_db"

# Configuracion del retriver
SEARCH_TYPE = "mmr"
MMR_DIVERSITY_LAMBDA = 0.7
MMR_FETCH_K = 20
SEARCH_K = 2


