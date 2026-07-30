import os
from uuid import uuid4
from pathlib import Path

from dotenv import load_dotenv
from langchain.chains import RetrievalQAWithSourcesChain
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings

os.environ["ANONYMIZED_TELEMETRY"] = "False"

load_dotenv()

# ==========================
# Constants
# ==========================

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

EMBEDDING_MODEL = "Alibaba-NLP/gte-base-en-v1.5"

VECTORSTORE_DIR = Path(__file__).parent / "resources" / "vectorstore"

COLLECTION_NAME = "real_estate"

llm = None
vector_store = None


# ==========================
# Initialize Components
# ==========================

def initialize_components():
    global llm, vector_store

    if llm is None:
        llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            temperature=0.2,
            max_tokens=500
        )

    if vector_store is None:

        embedding_model = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL,
            model_kwargs={"trust_remote_code": True}
        )

        vector_store = Chroma(
            collection_name=COLLECTION_NAME,
            embedding_function=embedding_model,
            persist_directory=str(VECTORSTORE_DIR)
        )


# ==========================
# Process URLs
# ==========================

def process_urls(urls):

    initialize_components()

    # Remove previous data
    vector_store.reset_collection()

    loader = UnstructuredURLLoader(urls=urls)

    print("Loading URLs...")
    data = loader.load()

    print(f"Loaded {len(data)} documents")

    if len(data) == 0:
        raise Exception("No content could be extracted from the URLs.")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", ".", " "]
    )

    docs = splitter.split_documents(data)

    print(f"Created {len(docs)} chunks")

    ids = [str(uuid4()) for _ in docs]

    vector_store.add_documents(
        documents=docs,
        ids=ids
    )

    print("Documents stored:", vector_store._collection.count())


# ==========================
# Generate Answer
# ==========================

def generate_answer(query):

    initialize_components()

    if vector_store._collection.count() == 0:
        return "Please process some URLs first.", ""

    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3}
    )

    # Debug
    retrieved_docs = retriever.invoke(query)

    print("\nRetrieved Documents\n")

    for i, doc in enumerate(retrieved_docs, start=1):
        print("=" * 80)
        print(doc.metadata)
        print(doc.page_content[:300])

    chain = RetrievalQAWithSourcesChain.from_llm(
        llm=llm,
        retriever=retriever
    )

    result = chain.invoke(
        {"question": query},
        return_only_outputs=True
    )

    print("\nLLM OUTPUT\n")
    print(result)

    answer = result.get("answer", "")
    sources = result.get("sources", "")

    return answer, sources


# ==========================
# Testing
# ==========================

if __name__ == "__main__":

    urls = [
        "https://www.thehindu.com/business/markets/rupee-gains-16-paise-to-9566-against-us-dollar/article71281317.ece",
        "https://www.cnbc.com/2026/07/28/stock-market-today-live-updates.html"
    ]

    process_urls(urls)

    answer, source = generate_answer(
        "Why did the rupee gain against the dollar?"
    )

    print("\nANSWER\n")
    print(answer)

    print("\nSOURCES\n")
    print(source)