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

🧠 Overview

CKHAI-ASSISTANT is a production-grade Retrieval-Augmented Generation (RAG) system that lets you chat with your own documents. Upload PDFs, ask questions in plain English, and get accurate, context-grounded answers — with the underlying LLM running fully offline via Ollama or in the cloud via Groq for blazing-fast inference.


Built for privacy, speed, and real deployment — not just a notebook demo.



<div align="center">
  📄 Documents  ──▶  ✂️ Chunking  ──▶  🔢 Embeddings  ──▶  🗄️ Vector Store
                                                                  │
  💬 Answer  ◀──  🤖 LLM  ◀──  🔍 Semantic Retrieval  ◀──────────┘

</div>

🏗️ Architecture

#mermaid-r3kk-r1 { font-family: "Anthropic Sans", system-ui, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; font-size: 16px; fill: rgb(25, 25, 25); }
#mermaid-r3kk-r1 .edge-animation-slow { stroke-dashoffset: 900; animation: 50s linear 0s infinite normal none running dash; stroke-linecap: round; stroke-dasharray: 9, 5 !important; }
#mermaid-r3kk-r1 .edge-animation-fast { stroke-dashoffset: 900; animation: 20s linear 0s infinite normal none running dash; stroke-linecap: round; stroke-dasharray: 9, 5 !important; }
#mermaid-r3kk-r1 .error-icon { fill: rgb(204, 120, 92); }
#mermaid-r3kk-r1 .error-text { fill: rgb(51, 135, 163); stroke: rgb(51, 135, 163); }
#mermaid-r3kk-r1 .edge-thickness-normal { stroke-width: 1px; }
#mermaid-r3kk-r1 .edge-thickness-thick { stroke-width: 3.5px; }
#mermaid-r3kk-r1 .edge-pattern-solid { stroke-dasharray: 0; }
#mermaid-r3kk-r1 .edge-thickness-invisible { stroke-width: 0; fill: none; }
#mermaid-r3kk-r1 .edge-pattern-dashed { stroke-dasharray: 3; }
#mermaid-r3kk-r1 .edge-pattern-dotted { stroke-dasharray: 2; }
#mermaid-r3kk-r1 .marker { fill: rgb(145, 145, 141); stroke: rgb(145, 145, 141); }
#mermaid-r3kk-r1 .marker.cross { stroke: rgb(145, 145, 141); }
#mermaid-r3kk-r1 svg { font-family: "Anthropic Sans", system-ui, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; font-size: 16px; }
#mermaid-r3kk-r1 p { margin: 0px; }
#mermaid-r3kk-r1 .label { font-family: "Anthropic Sans", system-ui, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; color: rgb(25, 25, 25); }
#mermaid-r3kk-r1 .cluster-label text { fill: rgb(51, 135, 163); }
#mermaid-r3kk-r1 .cluster-label span { color: rgb(51, 135, 163); }
#mermaid-r3kk-r1 .cluster-label span p { background-color: transparent; }
#mermaid-r3kk-r1 .label text, #mermaid-r3kk-r1 span { fill: rgb(25, 25, 25); color: rgb(25, 25, 25); }
#mermaid-r3kk-r1 .node rect, #mermaid-r3kk-r1 .node circle, #mermaid-r3kk-r1 .node ellipse, #mermaid-r3kk-r1 .node polygon, #mermaid-r3kk-r1 .node path { fill: rgb(240, 240, 235); stroke: rgb(217, 216, 213); stroke-width: 1px; }
#mermaid-r3kk-r1 .rough-node .label text, #mermaid-r3kk-r1 .node .label text, #mermaid-r3kk-r1 .image-shape .label, #mermaid-r3kk-r1 .icon-shape .label { text-anchor: middle; }
#mermaid-r3kk-r1 .node .katex path { fill: rgb(0, 0, 0); stroke: rgb(0, 0, 0); stroke-width: 1px; }
#mermaid-r3kk-r1 .rough-node .label, #mermaid-r3kk-r1 .node .label, #mermaid-r3kk-r1 .image-shape .label, #mermaid-r3kk-r1 .icon-shape .label { text-align: center; }
#mermaid-r3kk-r1 .node.clickable { cursor: pointer; }
#mermaid-r3kk-r1 .root .anchor path { stroke-width: 0; stroke: rgb(145, 145, 141); fill: rgb(145, 145, 141) !important; }
#mermaid-r3kk-r1 .arrowheadPath { fill: rgb(11, 11, 11); }
#mermaid-r3kk-r1 .edgePath .path { stroke: rgb(145, 145, 141); stroke-width: 1px; }
#mermaid-r3kk-r1 .flowchart-link { stroke: rgb(145, 145, 141); fill: none; }
#mermaid-r3kk-r1 .edgeLabel { background-color: rgb(245, 230, 216); text-align: center; }
#mermaid-r3kk-r1 .edgeLabel p { background-color: rgb(245, 230, 216); }
#mermaid-r3kk-r1 .edgeLabel rect { opacity: 0.5; background-color: rgb(245, 230, 216); fill: rgb(245, 230, 216); }
#mermaid-r3kk-r1 .labelBkg { background-color: rgba(245, 230, 216, 0.5); }
#mermaid-r3kk-r1 .cluster rect { fill: rgb(204, 120, 92); stroke: rgb(138, 115, 107); stroke-width: 1px; }
#mermaid-r3kk-r1 .cluster text { fill: rgb(51, 135, 163); }
#mermaid-r3kk-r1 .cluster span { color: rgb(51, 135, 163); }
#mermaid-r3kk-r1 div.mermaidTooltip { position: absolute; text-align: center; max-width: 200px; padding: 2px; font-family: "Anthropic Sans", system-ui, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; font-size: 12px; background: rgb(204, 120, 92); border: 1px solid rgb(138, 115, 107); border-radius: 2px; pointer-events: none; z-index: 100; }
#mermaid-r3kk-r1 .flowchartTitleText { text-anchor: middle; font-size: 18px; fill: rgb(25, 25, 25); }
#mermaid-r3kk-r1 rect.text { fill: none; stroke-width: 0; }
#mermaid-r3kk-r1 .icon-shape, #mermaid-r3kk-r1 .image-shape { background-color: rgb(245, 230, 216); text-align: center; }
#mermaid-r3kk-r1 .icon-shape p, #mermaid-r3kk-r1 .image-shape p { background-color: rgb(245, 230, 216); padding: 2px; }
#mermaid-r3kk-r1 .icon-shape .label rect, #mermaid-r3kk-r1 .image-shape .label rect { opacity: 0.5; background-color: rgb(245, 230, 216); fill: rgb(245, 230, 216); }
#mermaid-r3kk-r1 .label-icon { display: inline-block; height: 1em; overflow: visible; vertical-align: -0.125em; }
#mermaid-r3kk-r1 .node .label-icon path { fill: currentcolor; stroke: revert; stroke-width: revert; }
#mermaid-r3kk-r1 .node .neo-node { stroke: rgb(217, 216, 213); }
#mermaid-r3kk-r1 [data-look="neo"].node rect, #mermaid-r3kk-r1 [data-look="neo"].cluster rect, #mermaid-r3kk-r1 [data-look="neo"].node polygon { stroke: url("#mermaid-r3kk-r1-gradient"); filter: drop-shadow(rgb(185, 185, 185) 1px 2px 2px); }
#mermaid-r3kk-r1 [data-look="neo"].node path { stroke: url("#mermaid-r3kk-r1-gradient"); stroke-width: 1px; }
#mermaid-r3kk-r1 [data-look="neo"].node .outer-path { filter: drop-shadow(rgb(185, 185, 185) 1px 2px 2px); }
#mermaid-r3kk-r1 [data-look="neo"].node .neo-line path { stroke: rgb(217, 216, 213); filter: none; }
#mermaid-r3kk-r1 [data-look="neo"].node circle { stroke: url("#mermaid-r3kk-r1-gradient"); filter: drop-shadow(rgb(185, 185, 185) 1px 2px 2px); }
#mermaid-r3kk-r1 [data-look="neo"].node circle .state-start { fill: rgb(0, 0, 0); }
#mermaid-r3kk-r1 [data-look="neo"].icon-shape .icon { fill: url("#mermaid-r3kk-r1-gradient"); filter: drop-shadow(rgb(185, 185, 185) 1px 2px 2px); }
#mermaid-r3kk-r1 [data-look="neo"].icon-shape .icon-neo path { stroke: url("#mermaid-r3kk-r1-gradient"); filter: drop-shadow(rgb(185, 185, 185) 1px 2px 2px); }
#mermaid-r3kk-r1 :root { --mermaid-font-family: "Anthropic Sans",system-ui,"Segoe UI",Roboto,Helvetica,Arial,sans-serif; }LocalCloud📄 PDF UploadDocument LoaderText Splitter / ChunkingEmbedding ModelChromaDBVector Store💬 User QueryEmbed QuerySimilarity SearchRetrieved ContextLLM Engine🦙 Ollama⚡ Groq✅ Grounded Answer


✨ Features

FeatureDescription🔒Local-First PrivacyRun the entire pipeline offline with Ollama — your documents never leave your machine⚡Cloud AccelerationSwitch to Groq for ultra-low-latency inference when you need speed🦜LangChain OrchestrationRobust RAG pipeline for loading, chunking, embedding, and retrieval🗄️Vector SearchChromaDB for fast, persistent semantic similarity search🚀FastAPI BackendClean, async REST API ready for production deployment📄Document Q&AUpload PDFs and ask natural-language questions with grounded answers🔄Pluggable LLMsSwap between local and cloud models with a config change


🛠️ Tech Stack

<div align="center">
LayerTechnologyAPIFastAPI · UvicornRAG FrameworkLangChainVector DBChromaDBLLM (Local)OllamaLLM (Cloud)GroqLanguagePython 3.10+

</div>

🚀 Getting Started

📋 Prerequisites


Python 3.10+
Ollama installed and running (for local mode)
A Groq API key (optional, for cloud mode)


⚙️ Installation

bash# 1. Clone the repository
git clone https://github.com/hotachandrakant/CKHAI-ASSISTANT.git
cd CKHAI-ASSISTANT

# 2. Create & activate a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables
cp .env.example .env            # then add your GROQ_API_KEY if using cloud mode

▶️ Running the App

The system runs three concurrent processes. Open three terminals (or use a process manager):

bash# Terminal 1 — start ChromaDB
chroma run --port 8000

# Terminal 2 — start Ollama (local LLM)
ollama serve

# Terminal 3 — launch the FastAPI server
uvicorn app:app --host 0.0.0.0 --port 8080 --reload

Then open http://localhost:8080/docs to explore the interactive API.


📡 API Endpoints

MethodEndpointDescriptionPOST/uploadUpload a PDF document for indexingPOST/askAsk a question against the indexed documentsGET/healthService health check


💡 Adjust the table above to match your actual route names.




🗺️ Roadmap


 Local RAG pipeline with Ollama
 Cloud inference with Groq
 FastAPI + ChromaDB integration
 Streaming responses
 Multi-document collections & namespaces
 Web UI front-end
 Docker Compose one-command deploy



🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a PR.


👤 Author

<div align="center">
Chandrakant Hota

Show Image
Show Image

Data Science & Full Stack Engineering

</div>

📝 License

This project is licensed under the MIT License — see the LICENSE file for details.

<!-- ====================== ANIMATED FOOTER ====================== -->
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:3B82F6,50:06B6D4,100:7C3AED&height=120&section=footer"/>
⭐ If you find this project useful, consider giving it a star! ⭐

</div>
