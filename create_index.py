from langchain_community.document_loaders import TextLoader # Or relevant loader for your SOPs
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os # Import os to help with paths if needed

def create_and_save_index():
    # Define the path to your raw hospital SOP documents
    # IMPORTANT: Replace 'path/to/your/sop_documents_folder' with the actual path
    # where your hospital SOP documents (e.g., .txt, .pdf, .docx files) are located.
    # For example, if your SOPs are in D:\Cakra\project\hospital_rag_chatbot\data\
    # you might use: documents_path = "data"
    documents_path = "D:/Cakra/project/hospital_rag_chatbot" # <--- YOU MUST CHANGE THIS!

    # --- Choose and configure your document loader based on your SOP file types ---
    # Example for loading ALL .txt files from a directory:
    from langchain_community.document_loaders import DirectoryLoader
    loader = DirectoryLoader(documents_path, glob="**/*.txt", show_progress=True)
    
    # Example for loading a single .txt file:
    # loader = TextLoader(os.path.join(documents_path, "my_sop.txt")) 
    
    # Example for loading PDFs: (requires 'pip install pypdf')
    # from langchain_community.document_loaders import PyPDFLoader
    # loader = DirectoryLoader(documents_path, glob="**/*.pdf", loader_cls=PyPDFLoader, show_progress=True)

    print(f"Loading documents from: {documents_path}...")
    documents = loader.load()
    print(f"Loaded {len(documents)} documents.")

    # 2. Split documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_documents(documents)
    print(f"Split into {len(texts)} chunks.")

    # 3. Initialize embeddings
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    print("Embedding model initialized.")

    # 4. Create the FAISS index
    print("Creating FAISS index from documents... This might take a while.")
    db = FAISS.from_documents(texts, embedding)
    print("FAISS index created.")

    # 5. Save the index to the correct location
    # This will create a 'hospital_index' directory in the current working directory
    # when you run this script.
    save_path = "hospital_index"
    db.save_local(save_path)
    print(f"FAISS index saved to {save_path}")

if __name__ == "__main__":
    create_and_save_index()