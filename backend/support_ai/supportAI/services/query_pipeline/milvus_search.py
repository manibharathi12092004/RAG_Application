import os
from dotenv import load_dotenv
from pymilvus import connections, Collection

load_dotenv()

ZILLIZ_URL = os.getenv("ZILLIZ_URL")
ZILLIZ_API_KEY = os.getenv("ZILLIZ_API_KEY")
ZILLIZ_DB_NAME = os.getenv("ZILLIZ_DB_NAME")


# Connect to Zilliz Cloud FIRST
connections.connect(
    alias="default",
    uri=ZILLIZ_URL,
    token=ZILLIZ_API_KEY,
    db_name=ZILLIZ_DB_NAME,
    secure=True
)


# Load collection
collection = Collection(
    "subscription_policies"
)

collection.load()


def search_milvus(
    embedding,
    provider,
    intent
):

    expr = (
        f'provider == "{provider.lower() + " subscription policy"}" '
        f'&& policy_type == "{intent}"'
    )

    results = collection.search(
        data=[embedding],
        anns_field="embedding",
        param={
            "metric_type": "COSINE",
            "params": {
                "nprobe": 10
            }
        },
        limit=5,
        expr=expr,
        output_fields=["text"]
    )

    if not results or not results[0]:
        return []

    docs = []

    for hit in results[0]:
        docs.append(
            hit.entity.get("text")
        )

    return docs