from supportAI.services.llm.llm_client import llm_chat


def generate_answer(
    question,
    subscription,
    policies
):

    # Convert lists/dicts to readable text
    policies_text = "\n\n".join(policies) if policies else "No policy found."

    subscription_text = (
        str(subscription)
        if subscription
        else "No active subscription information available."
    )

    prompt = f"""
You are a professional SaaS Support Assistant.

Use ONLY the provided policies and subscription information
to answer the customer question.

Policies:
{policies_text}

Customer Subscription:
{subscription_text}

Customer Question:
{question}

Give a clear, helpful, and concise answer.
"""

    response = llm_chat(prompt)

    return response