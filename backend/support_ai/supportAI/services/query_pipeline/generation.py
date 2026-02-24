from supportAI.services.llm.llm_client import llm_chat


def generate_answer(
    question,
    subscription,
    policies
):

    # Compose hidden context for LLM only
    policy_context = "\n\n".join(policies) if policies else ""
    subscription_text = str(subscription) if subscription else ""

    prompt = f"""
You are PolicyMind AI, a SaaS subscription support assistant.

Use the provided policy context and customer subscription information internally to reason.

DO NOT mention retrieved documents or policies explicitly.
DO NOT output tables.
DO NOT list possible scenarios unless necessary.

Provide a short, clear, conversational explanation answering the customer question.

Policy Context (for internal use only):
{policy_context}

Customer Subscription (for internal use only):
{subscription_text}

Customer Question:
{question}
"""

    response = llm_chat(prompt)
    return response.strip()