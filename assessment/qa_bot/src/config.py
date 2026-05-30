# ==================================
# OLLAMA SETTINGS
# ==================================

LLM_MODEL = "llama3.2"

EMBED_MODEL = "nomic-embed-text"

OLLAMA_BASE_URL = "http://localhost:11434"


# ==================================
# CHUNKING SETTINGS
# ==================================

CHUNK_SIZE = 500

CHUNK_OVERLAP = 100


# ==================================
# RETRIEVAL SETTINGS
# ==================================

TOP_K = 3


# ==================================
# PATHS
# ==================================

UPLOAD_FOLDER = "data/uploaded_docs"

VECTOR_DB_PATH = "chroma_db"