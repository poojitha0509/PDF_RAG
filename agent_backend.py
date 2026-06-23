from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore
import tempfile

COLLECTION_NAME = "pdf_chatbot_v1"


def process_pdf(uploaded_file):

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as tmp:

        tmp.write(uploaded_file.read())
        pdf_path = tmp.name

    # Load PDF
    loader = PyPDFLoader(file_path=pdf_path)
    pages = loader.load()

    # Split PDF into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = text_splitter.split_documents(pages)

    # Embeddings
    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )

    # Store in Qdrant
    QdrantVectorStore.from_documents(
        documents=chunks,
        url="http://localhost:6333",
        collection_name=COLLECTION_NAME,
        embedding=embeddings,
        force_recreate=True
    )

    return "PDF processed successfully"


def search_pdf(query):

    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )

    retriever = QdrantVectorStore.from_existing_collection(
        embedding=embeddings,
        collection_name=COLLECTION_NAME,
        url="http://localhost:6333"
    )

    found_docs = retriever.similarity_search(
        query,
        k=3
    )

    return found_docs