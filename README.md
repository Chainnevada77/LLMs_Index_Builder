## create_index.py

Create vector and metadata indexes (`index.faiss`, `index.pkl`) from your document collection.  
Built for efficient retrieval and search use cases in LLM pipelines (e.g. RAG, QA systems).
---
## 📦 Outputs
| File              | Description                              |
|-------------------|------------------------------------------|
| `index.faiss`     | Vector store built with FAISS            |
| `index.pkl`       | Metadata store (e.g., chunk mappings)    |
| Folder: `llm_index/` | Contains both files above            |
---
## 🚀 Usage

1. Install dependencies
pip install langchain faiss-cpu sentence-transformers tqdm
or
pip install requirements.txt

2. Before running, update this line in the script:

documents_path = "/home/cakra_ai_dev/projects/hospital_rag_chatbot" # <--- YOU MUST CHANGE THIS!
#in my case path and has been using conda inside WSL

3. Run the script
python create_index.py

'''bash
🛠 Script Highlights
Loads documents from a directory (.txt by default).
Splits text using RecursiveCharacterTextSplitter.
Embeds using sentence-transformers/all-MiniLM-L6-v2.
Builds FAISS vector index.
Saves to llm_index/ folder.

🧱 Folder Structure
├── create_index.py
├── requirements.txt
├── license.txt
├── llm_index/         # Output files
│   ├── index.faiss
│   └── index.pkl
└── README.md

📜 License
MIT License
