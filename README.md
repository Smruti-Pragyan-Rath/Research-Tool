# Research Tool

A Retrieval-Augmented Generation (RAG) application that allows users to ask questions about news articles by providing their URLs. Instead of relying only on the language model's knowledge, the application retrieves relevant information from the supplied articles and generates answers based on that context.

This project was built to understand the fundamentals of RAG systems and how components like **LangChain**, **Groq**, **Chroma Vector Database**, and **embeddings** work together in a complete retrieval pipeline.

---
## Screenshot of Working Website
<img width="1727" height="706" alt="image" src="https://github.com/user-attachments/assets/1e191dba-7969-45ce-ae3a-0c5e4ee62a1e" />


## Table of Contents

- [Features](#features)
- [How RAG Works](#how-rag-works)
- [Project Pipeline](#project-pipeline)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Example Workflow](#example-workflow)
- [Concepts Covered](#concepts-covered)
- [Future Improvements](#future-improvements)

---

## Features

- Extracts content from news article URLs
- Automatically splits long documents into smaller chunks
- Generates vector embeddings using HuggingFace models
- Stores embeddings in a Chroma Vector Database
- Performs semantic similarity search
- Retrieves the most relevant document chunks
- Generates answers using the Groq LLM
- Displays the sources used for answering the query

---

## How RAG Works

Retrieval-Augmented Generation (RAG) combines **information retrieval** with **Large Language Models (LLMs)**.

Instead of answering from the model's pre-trained knowledge alone, the application first searches through the provided documents, retrieves the most relevant information, and then sends that context to the LLM to generate a grounded response.

This approach helps reduce hallucinations and allows the model to answer questions about documents it has never seen before.

---

## Project Pipeline

```
User enters News URLs
          │
          ▼
Load Articles
(UnstructuredURLLoader)
          │
          ▼
Split Documents
(RecursiveCharacterTextSplitter)
          │
          ▼
Generate Embeddings
(HuggingFace Embeddings)
          │
          ▼
Store Embeddings
(Chroma Vector Database)
          │
          ▼
User asks a Question
          │
          ▼
Similarity Search
(Retriever)
          │
          ▼
Relevant Chunks Retrieved
          │
          ▼
Groq LLM
          │
          ▼
Answer + Source Documents
```

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Streamlit | User Interface |
| LangChain | Building the RAG pipeline |
| Groq | Large Language Model inference |
| HuggingFace Embeddings | Text embedding generation |
| Chroma | Vector Database |
| dotenv | Environment variable management |
| UnstructuredURLLoader | Loading article content |

---

## Project Structure

```
News-Research-Tool/
│
├── app.py                 # Streamlit application
├── rag.py                 # RAG pipeline
├── requirements.txt
├── .env
├── vector_db/             # Chroma database
├── README.md
└── assets/
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/news-research-tool.git
cd news-research-tool
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

```env
GROQ_API_KEY=your_api_key_here
```

### 5. Run the application

```bash
streamlit run app.py
```

---

## Usage

1. Launch the Streamlit application.
2. Enter one or more news article URLs.
3. Click **Process URLs**.
4. Wait while the articles are processed and stored in the vector database.
5. Enter a question related to the uploaded articles.
6. The application retrieves relevant information and generates an answer along with the source documents.

---

## Example Workflow

Suppose the application processes articles about artificial intelligence.

**Question**

> Which company announced a new AI model?

The application performs the following steps:

- Converts the question into an embedding
- Searches the Chroma Vector Database
- Retrieves the most relevant text chunks
- Passes those chunks to the Groq LLM
- Generates an answer using only the retrieved context
- Displays the source articles used to produce the response

---

## Concepts Covered

This project demonstrates several important concepts used in modern Retrieval-Augmented Generation systems:

- Document Loading
- Text Chunking
- Embeddings
- Semantic Search
- Vector Databases
- Similarity Search
- Retrieval Pipelines
- Prompt Grounding
- LangChain Chains
- Retrievers
- Large Language Models
- Context-Aware Question Answering

---

## Why Chroma?

Traditional databases search for exact keywords.

Vector databases like **Chroma** search based on semantic similarity.

For example:

**Query**

> Which company reduced its workforce?

can successfully retrieve a document containing

> The organization announced layoffs.

even if the exact word *workforce* never appears.

This semantic search capability is one of the key reasons vector databases are widely used in RAG applications.

---

## Future Improvements

- Support PDF documents
- Upload local files
- Store conversation history
- Hybrid search (Keyword + Vector Search)
- Metadata filtering
- Multiple embedding model support
- Streaming responses
- Docker deployment
- Retrieval evaluation metrics
- Multi-document summarization

---

## Learning Outcomes

Building this project helped me understand:

- The architecture of a Retrieval-Augmented Generation (RAG) system
- How LangChain connects different components of a retrieval pipeline
- How embeddings represent semantic meaning
- Why vector databases are used for document retrieval
- How similarity search improves answer relevance
- How retrieved context helps reduce hallucinations in LLM responses
- How Groq can be integrated for fast LLM inference
- The complete flow from document ingestion to answer generation

---

## Acknowledgements

- LangChain
- Groq
- Chroma
- HuggingFace
- Streamlit

---

## License

This project is intended for learning and educational purposes.
