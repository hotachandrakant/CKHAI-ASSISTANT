import structlog
from langchain_community.llms import Ollama
from app.services.ingestion import get_vector_store
from app.models.schemas import QueryResponse, SourceDocument
from app.config import get_settings
from datetime import datetime

logger = structlog.get_logger()
settings = get_settings()

CASUAL_WORDS = {
    "hello", "hi", "hey", "hii", "helo", "sup", "yo", "howdy",
    "how are you", "whats up", "what's up", "good morning", "good evening",
    "good afternoon", "good night", "bye", "goodbye", "thanks", "thank you",
    "i love you", "love you", "why", "ok", "okay", "yes", "no", "sure",
    "cool", "nice", "great", "awesome", "wow", "lol", "haha", "who are you",
    "what are you", "introduce yourself", "what can you do"
}


def is_casual(question: str) -> bool:
    q = question.lower().strip().rstrip("?!.")
    return q in CASUAL_WORDS or len(q.split()) <= 2


async def answer_question(
    question: str,
    collection_name: str = None,
    top_k: int = 5,
) -> QueryResponse:
    logger.info("query_started", question=question[:80])

    docs = []
    context = ""

    if not is_casual(question):
        try:
            vector_store = get_vector_store(collection_name)
            retriever = vector_store.as_retriever(
                search_type="mmr",
                search_kwargs={"k": top_k, "fetch_k": top_k * 2},
            )
            docs = retriever.invoke(question)
            context = "\n\n".join([d.page_content for d in docs])
        except Exception:
            pass

    if context.strip():
        prompt = f"""You are CKHai, an expert AI tutor. Answer using the document AND your own knowledge.

Rules:
- Answer directly and helpfully. Never refuse.
- Use **bold** for headings
- Numbered lists for steps
- Bullet points for features
- Code blocks for code

Document context:
{context}

Question: {question}

Answer:"""
    else:
        prompt = f"""You are CKHai, a friendly AI assistant like ChatGPT.

Rules:
- Always reply warmly and helpfully
- For greetings, introduce yourself nicely as CKHai
- Use **bold**, bullet points, emojis naturally
- Be positive and conversational
- NEVER bring up unrelated topics

User: {question}

CKHai:"""

    llm = Ollama(
        model="llama3.2",
        base_url="http://localhost:11434",
        temperature=0.4,
    )

    answer = await llm.ainvoke(prompt)

    sources = []
    seen = set()
    for doc in docs:
        key = doc.metadata.get("source", "") + str(doc.metadata.get("page", ""))
        if key not in seen:
            seen.add(key)
            sources.append(SourceDocument(
                page_content=doc.page_content[:400],
                source=doc.metadata.get("source", "unknown"),
                page=doc.metadata.get("page"),
            ))

    logger.info("query_complete", sources_returned=len(sources))

    return QueryResponse(
        answer=answer,
        sources=sources[:3],
        question=question,
        model="llama3.2",
        timestamp=datetime.utcnow(),
    )