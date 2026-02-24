from supportAI.services.query_pipeline.query_translation import translate_query

from supportAI.services.query_pipeline.postgres_context import fetch_user_context

from supportAI.services.query_pipeline.query_structurer import structure_query

from supportAI.services.query_pipeline.embedding_service import embed_query

from supportAI.services.query_pipeline.milvus_search import search_milvus

from supportAI.services.query_pipeline.generation import generate_answer



def process(question, user_id):

    # STEP 1 — Translate Query
    translated = translate_query(question)


    # STEP 2 — Fetch User Subscription Context (Neon/Postgres)
    subscriptions = fetch_user_context(user_id)


    # STEP 3 — Structure Query (Intent + Provider)
    structured = structure_query(
        translated,
        subscriptions
    )

    provider = structured.get("provider")
    intent = structured.get("intent")


    # STEP 4 — Generate Embedding
    embedding = embed_query(translated)


    # STEP 5 — Milvus Retrieval
    policies = search_milvus(
        embedding,
        provider,
        intent
    )


    # STEP 6 — Generate Final Answer
    answer = generate_answer(
        question,
        subscriptions,
        policies
    )

    return {
        "answer": answer
    }