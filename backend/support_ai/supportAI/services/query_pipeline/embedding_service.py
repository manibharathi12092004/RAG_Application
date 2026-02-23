import os
import requests
from dotenv import load_dotenv

load_dotenv()

OLLAMA_EMBED_HOST = os.getenv("OLLAMA_EMBED_HOST")
EMBED_MODEL = os.getenv("EMBED_MODEL")


def embed_query(query: str):

    url = f"{OLLAMA_EMBED_HOST}"

    print("URL =", url)

    response = requests.post(
        url,
        json={
            "model": EMBED_MODEL,
            "input": query
        },
        timeout=60
    )

    response.raise_for_status()

    data = response.json()

    print("DEBUG:", data)  # remove later

    # Ollama returns single embedding
    return data["embeddings"][0]