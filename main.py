from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_community.document_loaders import OnlinePDFLoader

local_path = "alchemist.pdf"

# Local PDF file
if local_path:
    loader = UnstructuredPDFLoader(file_path=local_path)
    data = loader.load()
    print(f"Loaded {len(data)} documents from local PDF.")
else:
    print("Upload a local PDF file to proceed.")

# Preview this data
print(data[0].page_content[:500])