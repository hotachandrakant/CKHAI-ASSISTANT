<!-- ==================== ANIMATED 3D BANNER ==================== -->
<div align="center">

<img src="./assets/banner.svg" width="100%" alt="CKHAI-ASSISTANT"/>

<!-- Typing animation -->
<a href="https://github.com/hotachandrakant/CKHAI-ASSISTANT">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=A78BFA&center=true&vCenter=true&width=620&lines=Chat+with+your+own+documents+%F0%9F%93%84;Retrieval-Augmented+Generation+pipeline+%F0%9F%A6%9C;100%25+local+%26+private+with+Ollama+%F0%9F%94%92;Cloud-fast+inference+with+Groq+%E2%9A%A1" alt="Typing SVG" />
</a>

<br/><br/>

<!-- Tech badges -->
<p>
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
  <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white"/>
  <img src="https://img.shields.io/badge/ChromaDB-FF6B6B?style=for-the-badge&logo=chromadb&logoColor=white"/>
  <img src="https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logo=ollama&logoColor=white"/>
  <img src="https://img.shields.io/badge/Groq-F55036?style=for-the-badge&logo=groq&logoColor=white"/>
</p>

<p>
  <img src="https://img.shields.io/github/stars/hotachandrakant/CKHAI-ASSISTANT?style=social"/>
  <img src="https://img.shields.io/github/forks/hotachandrakant/CKHAI-ASSISTANT?style=social"/>
  <img src="https://img.shields.io/github/last-commit/hotachandrakant/CKHAI-ASSISTANT?color=A78BFA&style=flat-square"/>
  <img src="https://img.shields.io/github/repo-size/hotachandrakant/CKHAI-ASSISTANT?color=22D3EE&style=flat-square"/>
  <img src="https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square"/>
</p>

</div>

<!-- Animated divider -->
<img src="https://raw.githubusercontent.com/Anmol-Baranwal/Cool-GIFs-For-GitHub/main/Lines/2.gif" width="100%"/>

## 🧠 What is CKHAI-ASSISTANT?

**CKHAI-ASSISTANT** is a production-grade **Retrieval-Augmented Generation (RAG)** system that turns any pile of PDFs into a conversational knowledge base. Upload your documents, ask questions in plain English, and get **accurate, source-grounded answers** — no hallucinated guesses.

The killer feature: it runs **100% offline** on your own machine via **Ollama**, so sensitive documents never leave your device — or flips to **Groq** in the cloud when you want answers at lightning speed.

> 💡 Not a notebook toy — a real FastAPI service with a vector store, retrieval pipeline, and swappable LLM backends.

<br/>

<div align="center">

| 🔒 Private by default | ⚡ Cloud when you need it | 📄 Grounded answers | 🚀 Production-ready API |
|:---:|:---:|:---:|:---:|
| Local LLM via Ollama | Groq for low latency | Cites your own docs | FastAPI + async |

</div>

<img src="https://raw.githubusercontent.com/Anmol-Baranwal/Cool-GIFs-For-GitHub/main/Lines/2.gif" width="100%"/>

## 🏗️ System Architecture

```mermaid
flowchart LR
    subgraph Ingestion["📥 Ingestion Pipeline"]
        A[📄 PDF Upload] --> B[Document Loader]
        B --> C[Recursive Text Splitter]
        C --> D[Embedding Model]
        D --> E[(🗄️ ChromaDB<br/>Vector Store)]
    end

    subgraph Query["💬 Query Pipeline"]
        Q[User Question] --> F[Embed Query]
        F --> G[Top-K Similarity Search]
        E --> G
        G --> H[Context + Prompt]
        H --> I{LLM Router}
        I -->|local| J[🦙 Ollama]
        I -->|cloud| K[⚡ Groq]
        J --> L[✅ Grounded Answer]
        K --> L
    end

    style E fill:#7C3AED,color:#fff,stroke:#A78BFA
    style I fill:#06B6D4,color:#fff,stroke:#22D3EE
    style L fill:#10B981,color:#fff,stroke:#34D399
```

<img src="https://raw.githubusercontent.com/Anmol-Baranwal/Cool-GIFs-For-GitHub/main/Lines/2.gif" width="100%"/>

## ✨ Features

| | Feature | Description |
|---|---------|-------------|
| 🔒 | **Local-First Privacy** | Full pipeline runs offline with Ollama — documents never leave your machine |
| ⚡ | **Cloud Acceleration** | One config switch to Groq for ultra-low-latency inference |
| 🔄 | **Pluggable LLM Backends** | Local ↔ cloud with zero code changes |
| 🦜 | **LangChain Orchestration** | Battle-tested load → chunk → embed → retrieve pipeline |
| 🗄️ | **Persistent Vector Search** | ChromaDB keeps embeddings across restarts |
| 📄 | **Source-Grounded Q&A** | Answers are anchored to retrieved chunks, not made up |
| 🚀 | **Async FastAPI Backend** | Clean REST API with auto-generated Swagger docs |
| 🧩 | **Configurable Retrieval** | Tune chunk size, overlap, and top-K from one place |

<img src="https://raw.githubusercontent.com/Anmol-Baranwal/Cool-GIFs-For-GitHub/main/Lines/2.gif" width="100%"/>

## 🛠️ Tech Stack

<div align="center">

<img src="https://skillicons.dev/icons?i=python,fastapi,docker,git,vscode&theme=dark" />

| Layer | Technology |
|-------|-----------|
| **API / Server** | FastAPI · Uvicorn |
| **RAG Framework** | LangChain |
| **Vector Database** | ChromaDB |
| **LLM — Local** | Ollama |
| **LLM — Cloud** | Groq |
| **Language** | Python 3.10+ |

</div>

<img src="https://raw.githubusercontent.com/Anmol-Baranwal/Cool-GIFs-For-GitHub/main/Lines/2.gif" width="100%"/>

## 📂 Project Structure

```
CKHAI-ASSISTANT/
├── assets/
│   └── banner.svg          # Animated banner
├── app.py                  # FastAPI entry point
├── rag/
│   ├── ingest.py           # Load, chunk & embed documents
│   ├── retriever.py        # Vector similarity search
│   └── llm.py              # Ollama / Groq router
├── data/                   # Uploaded source documents
├── chroma_db/              # Persistent vector store
├── .env.example            # Environment template
├── requirements.txt
└── README.md
```
> 📝 Adjust file/folder names to match your actual layout.

<img src="https://raw.githubusercontent.com/Anmol-Baranwal/Cool-GIFs-For-GitHub/main/Lines/2.gif" width="100%"/>

## 🚀 Getting Started

### 📋 Prerequisites
- Python **3.10+**
- [Ollama](https://ollama.com) installed & running — for local mode
- A [Groq API key](https://console.groq.com) — optional, for cloud mode

### ⚙️ Installation

```bash
# 1 — Clone
git clone https://github.com/hotachandrakant/CKHAI-ASSISTANT.git
cd CKHAI-ASSISTANT

# 2 — Virtual environment
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate

# 3 — Dependencies
pip install -r requirements.txt

# 4 — Environment
cp .env.example .env              # add GROQ_API_KEY if using cloud mode
```

### ▶️ Run (3 concurrent services)

```bash
# Terminal 1 — Vector store
chroma run --port 8000

# Terminal 2 — Local LLM
ollama serve

# Terminal 3 — API server
uvicorn app:app --host 0.0.0.0 --port 8080 --reload
```

Open **http://localhost:8080/docs** for the interactive Swagger UI. 🎉

<img src="https://raw.githubusercontent.com/Anmol-Baranwal/Cool-GIFs-For-GitHub/main/Lines/2.gif" width="100%"/>

## ⚙️ Configuration

| Variable | Description | Default |
|----------|-------------|---------|
| `LLM_PROVIDER` | `ollama` or `groq` | `ollama` |
| `OLLAMA_MODEL` | Local model name | `llama3` |
| `GROQ_API_KEY` | Groq cloud key | — |
| `CHUNK_SIZE` | Tokens per chunk | `1000` |
| `CHUNK_OVERLAP` | Overlap between chunks | `200` |
| `TOP_K` | Chunks retrieved per query | `4` |
> Map these to your real settings/env names.

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/upload` | Upload & index a PDF |
| `POST` | `/ask` | Ask a question over indexed docs |
| `GET`  | `/health` | Service health check |

<img src="https://raw.githubusercontent.com/Anmol-Baranwal/Cool-GIFs-For-GitHub/main/Lines/2.gif" width="100%"/>

## 🗺️ Roadmap

- [x] Local RAG pipeline with Ollama
- [x] Cloud inference with Groq
- [x] FastAPI + ChromaDB integration
- [ ] Streaming token responses
- [ ] Multi-document collections / namespaces
- [ ] Web UI front-end
- [ ] Docker Compose one-command deploy

## 🤝 Contributing

Contributions, issues, and feature requests are welcome — open an issue or submit a PR.

<img src="https://raw.githubusercontent.com/Anmol-Baranwal/Cool-GIFs-For-GitHub/main/Lines/2.gif" width="100%"/>

## 👤 Author

<div align="center">

**Chandrakant Hota**

[![GitHub](https://img.shields.io/badge/GitHub-hotachandrakant-181717?style=for-the-badge&logo=github)](https://github.com/hotachandrakant)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/hotachandrakant)

*Data Science & Full Stack Engineering*

</div>

## 📝 License

Licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

<div align="center">

⭐ **If this project helped you, drop a star!** ⭐

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:3B82F6,50:06B6D4,100:7C3AED&height=110&section=footer"/>

</div>
