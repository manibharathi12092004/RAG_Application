import json

from supportAI.services.llm.llm_client import llm_chat


def structure_query(

 translated_query,

 subscriptions

):

 prompt=f"""

You are SaaS AI Orchestrator.

Customer subscriptions:

{subscriptions}

Customer search query:

{translated_query}

Decide:

1 Intent (billing/refund/cancellation)

2 Which provider subscription is relevant.

3 Whether subscription data required.

4 Give provider name always small letters.

Return JSON ONLY:

{{
"intent":"",
"provider":"",
"requires_subscription":true
}}

"""

 response=llm_chat(prompt)

 return json.loads(response)

