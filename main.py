from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_community.document_loaders import OnlinePDFLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma

local_path = "alchemist.pdf"

# Local PDF file
if local_path:
    loader = UnstructuredPDFLoader(file_path=local_path)
    data = loader.load()
    print(f"Loaded {len(data)} documents from local PDF.")
else:
    print("Upload a local PDF file to proceed.")

# Split the text into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=7500, chunk_overlap=100)
chunks = text_splitter.split_documents(data)

vector_db = Chroma.from_documents(
    documents=chunks,
    embedding=OllamaEmbeddings(model="nomic-embed-text", show_progress=True),
    collection_name="pdf-collection",
)



