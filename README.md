## Project Description

Document Q&A Bot is a Retrieval-Augmented Generation (RAG) application that allows users to upload PDF, DOCX, and TXT documents and ask questions based on their contents. The system retrieves the most relevant document chunks using semantic search and generates accurate answers using a local Ollama Large Language Model.

The application uses a persistent ChromaDB vector database, enabling document indexing only once and allowing efficient retrieval across application restarts.

---

# Tech Stack

| Component       | Technology                     | Version           |
| --------------- | ------------------------------ | ----------------- |
| Frontend        | Streamlit                      | Latest            |
| LLM             | Ollama (llama3.2)              | Latest            |
| Embedding Model | nomic-embed-text               | Latest            |
| Framework       | LangChain                      | Latest            |
| Vector Database | ChromaDB                       | Latest            |
| PDF Loader      | PyPDF                          | Latest            |
| DOCX Loader     | docx2txt                       | Latest            |
| Chunking        | RecursiveCharacterTextSplitter | LangChain         |
| Testing         | Pytest                         | Latest            |
| Language        | Python                         | 3.11+ Recommended |

---

# Architecture Overview

## RAG Pipeline

```text
User Uploads Documents
           │
           ▼
Document Loader
(PDF / DOCX / TXT)
           │
           ▼
Text Chunking
           │
           ▼
Embedding Generation
(nomic-embed-text)
           │
           ▼
ChromaDB Vector Store
           │
           ▼
User Question
           │
           ▼
Similarity Search
           │
           ▼
Top-K Relevant Chunks
           │
           ▼
LLM Generation
(llama3.2)
           │
           ▼
Answer Returned
```

### Components

1. Document Ingestion

   * Upload and load PDF, DOCX, and TXT files.

2. Chunking

   * Split large documents into smaller chunks.

3. Embedding

   * Convert chunks into vector representations using nomic-embed-text.

4. Retrieval

   * Perform similarity search in ChromaDB.

5. Generation

   * Use llama3.2 to generate context-aware responses.

---

# Chunking Strategy

## Strategy Used

RecursiveCharacterTextSplitter

### Configuration

```python
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100
```

### Why This Strategy?

* Preserves context between adjacent chunks.
* Prevents loss of information at chunk boundaries.
* Works effectively for both short and long documents.
* Provides a balance between retrieval accuracy and embedding cost.

The overlap ensures that important information spanning multiple chunks remains available during retrieval.

---

# Embedding Model and Vector Database

## Embedding Model

### nomic-embed-text

Reason for selection:

* Free and locally runnable through Ollama.
* High-quality semantic embeddings.
* No API costs.
* Good performance for retrieval tasks.

## Vector Database

### ChromaDB

Reason for selection:

* Lightweight and easy to integrate.
* Supports persistent storage.
* Fast similarity search.
* Open source.
* Works seamlessly with LangChain.

Persistence allows embeddings to remain available even after restarting the application.

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone <repository-url>
cd qa_bot
```

## 2. Create Virtual Environment

```bash
python -m venv venv
```

## 3. Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## 5. Install Ollama

Download and install Ollama:

https://ollama.com/download

## 6. Download Required Models

```bash
ollama pull llama3.2
```

```bash
ollama pull nomic-embed-text
```

## 7. Start Ollama

```bash
ollama serve
```

## 8. Run Application

```bash
streamlit run app.py
```

## 9. Open Browser

Navigate to:

```text
http://localhost:8501
```

---

# Environment Variables

This project uses local Ollama models and does not require paid API keys.

Create a `.env` file in the project root:

```env
OLLAMA_BASE_URL=http://localhost:11434
```

### Required Variables

| Variable        | Description            |
| --------------- | ---------------------- |
| OLLAMA_BASE_URL | Ollama server endpoint |

### Security Note

Never commit API keys, secrets, or credentials to version control.

---

# Example Queries

## Example 1

Question:

```text
Who founded the Mughal Empire?
```

Expected Theme:

```text
Historical founder information from uploaded history documents.
```

---

## Example 2

Question:

```text
What is machine learning?
```

Expected Theme:

```text
Definition and explanation from AI-related documents.
```

---

## Example 3

Question:

```text
Summarize the main findings of the report.
```

Expected Theme:

```text
Executive summary generated from uploaded report content.
```

---

## Example 4

Question:

```text
What are the cybersecurity threats discussed in the document?
```

Expected Theme:

```text
Security risks and recommendations extracted from uploaded files.
```

---

## Example 5

Question:

```text
Explain climate change impacts mentioned in the report.
```

Expected Theme:

```text
Environmental impacts and findings from climate-related documents.
```

---

# Known Limitations

## 1. Retrieval Accuracy Depends on Chunking

If relevant information is split across multiple chunks, retrieval quality may decrease.

---

## 2. Limited Context Window

The LLM can only process a finite amount of retrieved text at one time.

---

## 3. No OCR Support

Scanned PDFs containing images without selectable text are not currently supported.

---

## 4. Hallucination Risk

Although retrieval reduces hallucinations, the LLM may occasionally generate unsupported statements if relevant context is insufficient.

---

## 5. Local Resource Usage

Running embeddings and inference locally requires sufficient CPU and memory resources.

---

# Future Improvements

* Add OCR support for scanned PDFs.
* Support additional file formats.
* Add conversational memory.
* Implement hybrid search (keyword + semantic).
* Add source highlighting in answers.
* Deploy using Docker.

---

# Project Structure

```text
qa_bot/

├── app.py
├── requirements.txt
│
├── data/
│   └── uploaded_docs/
│
├── chroma_db/
│
├── src/
│   ├── config.py
│   ├── document_loader.py
│   ├── text_chunker.py
│   ├── embedding_model.py
│   ├── vector_store.py
│   ├── ingest.py
│   ├── retriever.py
│   ├── generator.py
│   ├── rag_pipeline.py
│   └── utils.py
│
└── tests/

