from rest_framework.decorators import api_view
from rest_framework.response import Response

from supportAI.services.rag.middleware import process


@api_view(["POST"])
def chat(request):

    user_id = request.data.get(
        "user_id"
    )

    question = request.data.get(
        "question"
    )

    if not user_id:

        return Response(
            {"error":"user_id required"},
            status=400
        )

    result = process(
        question,
        user_id
    )

    return Response(result)