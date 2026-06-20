<!-- ====================== ANIMATED HEADER ====================== -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:7C3AED,50:06B6D4,100:3B82F6&height=200&section=header&text=CKHAI-ASSISTANT&fontSize=55&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Production-Grade%20RAG%20Document%20Q%26A%20System&descAlignY=58&descSize=18" width="100%"/>

<!-- Typing animation -->
<a href="https://github.com/hotachandrakant/CKHAI-ASSISTANT">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=7C3AED&center=true&vCenter=true&width=600&lines=Chat+with+your+documents+%F0%9F%93%84;Powered+by+LangChain+%2B+ChromaDB+%F0%9F%A6%9C;Runs+100%25+local+with+Ollama+%F0%9F%92%BB;Cloud-ready+with+Groq+%E2%9A%A1" alt="Typing SVG" />
</a>

<br/>

<!-- Badges -->
<p>
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
  <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white"/>
  <img src="https://img.shields.io/badge/ChromaDB-FF6B6B?style=for-the-badge&logo=databricks&logoColor=white"/>
  <img src="https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logo=ollama&logoColor=white"/>
  <img src="https://img.shields.io/badge/Groq-F55036?style=for-the-badge&logo=groq&logoColor=white"/>
</p>

<p>
  <img src="https://img.shields.io/github/stars/hotachandrakant/CKHAI-ASSISTANT?style=social"/>
  <img src="https://img.shields.io/github/forks/hotachandrakant/CKHAI-ASSISTANT?style=social"/>
  <img src="https://img.shields.io/github/last-commit/hotachandrakant/CKHAI-ASSISTANT?color=7C3AED&style=flat-square"/>
  <img src="https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square"/>
</p>

</div>

---

## 🧠 Overview

**CKHAI-ASSISTANT** is a production-grade **Retrieval-Augmented Generation (RAG)** system that lets you **chat with your own documents**. Upload PDFs, ask questions in plain English, and get accurate, context-grounded answers — with the underlying LLM running **fully offline via Ollama** or in the **cloud via Groq** for blazing-fast inference.

> Built for privacy, speed, and real deployment — not just a notebook demo.

<div align="center">

```
  📄 Documents  ──▶  ✂️ Chunking  ──▶  🔢 Embeddings  ──▶  🗄️ Vector Store
                                                                  │
  💬 Answer  ◀──  🤖 LLM  ◀──  🔍 Semantic Retrieval  ◀──────────┘
```

</div>

---

## 🏗️ Architecture

```mermaid
flowchart LR
    A[📄 PDF Upload] --> B[Document Loader]
    B --> C[Text Splitter / Chunking]
    C --> D[Embedding Model]
    D --> E[(ChromaDB<br/>Vector Store)]

    Q[💬 User Query] --> F[Embed Query]
    F --> G[Similarity Search]
    E --> G
    G --> H[Retrieved Context]
    H --> I{LLM Engine}
    I -->|Local| J[🦙 Ollama]
    I -->|Cloud| K[⚡ Groq]
    J --> L[✅ Grounded Answer]
    K --> L

    style E fill:#7C3AED,color:#fff
    style I fill:#06B6D4,color:#fff
    style L fill:#10B981,color:#fff
```

---

## ✨ Features

| | Feature | Description |
|---|---------|-------------|
| 🔒 | **Local-First Privacy** | Run the entire pipeline offline with Ollama — your documents never leave your machine |
| ⚡ | **Cloud Acceleration** | Switch to Groq for ultra-low-latency inference when you need speed |
| 🦜 | **LangChain Orchestration** | Robust RAG pipeline for loading, chunking, embedding, and retrieval |
| 🗄️ | **Vector Search** | ChromaDB for fast, persistent semantic similarity search |
| 🚀 | **FastAPI Backend** | Clean, async REST API ready for production deployment |
| 📄 | **Document Q&A** | Upload PDFs and ask natural-language questions with grounded answers |
| 🔄 | **Pluggable LLMs** | Swap between local and cloud models with a config change |

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Technology |
|-------|-----------|
| **API** | FastAPI · Uvicorn |
| **RAG Framework** | LangChain |
| **Vector DB** | ChromaDB |
| **LLM (Local)** | Ollama |
| **LLM (Cloud)** | Groq |
| **Language** | Python 3.10+ |

</div>

---

## 🚀 Getting Started

### 📋 Prerequisites

- Python 3.10+
- [Ollama](https://ollama.com) installed and running (for local mode)
- A [Groq API key](https://console.groq.com) (optional, for cloud mode)

### ⚙️ Installation

```bash
# 1. Clone the repository
git clone https://github.com/hotachandrakant/CKHAI-ASSISTANT.git
cd CKHAI-ASSISTANT

# 2. Create & activate a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables
cp .env.example .env            # then add your GROQ_API_KEY if using cloud mode
```

### ▶️ Running the App

The system runs **three concurrent processes**. Open three terminals (or use a process manager):

```bash
# Terminal 1 — start ChromaDB
chroma run --port 8000

# Terminal 2 — start Ollama (local LLM)
ollama serve

# Terminal 3 — launch the FastAPI server
uvicorn app:app --host 0.0.0.0 --port 8080 --reload
```

Then open **http://localhost:8080/docs** to explore the interactive API.

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/upload` | Upload a PDF document for indexing |
| `POST` | `/ask` | Ask a question against the indexed documents |
| `GET`  | `/health` | Service health check |

> 💡 Adjust the table above to match your actual route names.

---

## 🗺️ Roadmap

- [x] Local RAG pipeline with Ollama
- [x] Cloud inference with Groq
- [x] FastAPI + ChromaDB integration
- [ ] Streaming responses
- [ ] Multi-document collections & namespaces
- [ ] Web UI front-end
- [ ] Docker Compose one-command deploy

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a PR.

---

## 👤 Author

<div align="center">

**Chandrakant Hota**

[![GitHub](https://img.shields.io/badge/GitHub-hotachandrakant-181717?style=for-the-badge&logo=github)](https://github.com/hotachandrakant)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/hotachandrakant)

*Data Science & Full Stack Engineering*

</div>

---

## 📝 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

<!-- ====================== ANIMATED FOOTER ====================== -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:3B82F6,50:06B6D4,100:7C3AED&height=120&section=footer"/>

⭐ **If you find this project useful, consider giving it a star!** ⭐

</div>
