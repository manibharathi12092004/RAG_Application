import os
import requests
from dotenv import load_dotenv

load_dotenv()

OLLAMA_HOST = os.getenv("OLLAMA_HOST")
OLLAMA_API_KEY = os.getenv("OLLAMA_API_KEY")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")


def translate_query(question):

    prompt = f"""
Rewrite the customer question into a clear SaaS support search query.

Question:
{question}

Return only improved search query.
"""

    response = requests.post(
        f"{OLLAMA_HOST}/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OLLAMA_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": OLLAMA_MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        },
        timeout=120
    )

    response.raise_for_status()

    data = response.json()

    return data["choices"][0]["message"]["content"]