# Create Index Data for LLMs

Generate `index.faiss` and `index.pkl` files from your dataset to power vector search or Retrieval-Augmented Generation (RAG) pipelines for Large Language Models (LLMs).
---
## 🧠 Overview

This repository contains a script (`create_index.py`) that processes input data, embeds it using a chosen model, and generates:

- `llm_index` folder  
- `index.faiss`: A FAISS vector index for fast similarity search.
- `index.pkl`: A pickle file storing metadata or document mapping.

These files can be used in downstream tasks such as:
- Retrieval-based chatbots
- Searchable knowledge bases
- RAG (Retrieval-Augmented Generation) pipelines
---
## 📂 Output Files

| File         | Description                              |
|--------------|------------------------------------------|
| `index.faiss` | FAISS index for vector similarity search |
| `index.pkl`   | Python Pickle storing metadata/doc IDs   |
---
## ⚙️ How It Works

```bash
python create_index.py --input data/your_data.json