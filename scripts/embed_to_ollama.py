import requests
import json
import time

# Import earlier pipeline
from embed_policies import create_documents
from extract_policies import read_all_policies


OLLAMA_URL = "http://localhost:11434/api/embeddings"

MODEL = "nomic-embed-text"

BATCH_SIZE = 10


# =====================================
# EMBEDDING FUNCTION
# =====================================

def embed_text(text):

    response = requests.post(

        OLLAMA_URL,

        json={

            "model": MODEL,

            "prompt": text

        }

    )

    if response.status_code != 200:

        raise Exception("Embedding Failed")

    return response.json()["embedding"]


# =====================================
# BATCH EMBEDDING
# =====================================

def embed_documents(documents):

    embedded_docs = []

    total = len(documents)

    for i in range(0, total, BATCH_SIZE):

        batch = documents[i:i+BATCH_SIZE]

        print(f"\nProcessing Batch {i} -> {i+len(batch)}")

        for doc in batch:

            embedding = embed_text(doc["text"])

            embedded_docs.append({

                "embedding": embedding,

                "text": doc["text"],

                "provider": doc["provider"],

                "policy_type": doc["policy_type"],

                "source_file": doc["source_file"],

                "chunk_id": doc["chunk_id"]

            })

        # small cooldown (important)
        time.sleep(1)

    return embedded_docs


# =====================================
# MAIN
# =====================================

if __name__ == "__main__":

    print("\nSTEP 10 — OLLAMA EMBEDDING STARTED\n")

    # STEP7
    policies = read_all_policies()

    # STEP8 + STEP9
    documents = create_documents(policies)

    print("\nCreating Embeddings...\n")

    embedded = embed_documents(documents)

    print("\nEmbedding Completed")

    print("Total Embedded:", len(embedded))


    # SAVE TEMP JSON

    with open("embedded_documents.json","w",encoding="utf-8") as f:

        json.dump(embedded,f,indent=2)


    print("\nSaved → embedded_documents.json")


    # sample output

    sample = embedded[0]

    print("\n===== SAMPLE EMBEDDING =====")

    print("Provider:",sample["provider"])

    print("Policy:",sample["policy_type"])

    print("Chunk:",sample["chunk_id"])

    print("Vector Length:",len(sample["embedding"]))