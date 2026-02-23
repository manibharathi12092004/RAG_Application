from supportAI.models import Subscription


def fetch_user_context(user_id):

    subs = Subscription.objects.filter(
        customer_id=user_id,
        status="active"
    )

    result = []

    for s in subs:
        result.append({
            "provider": s.provider,
            "plan": s.plan_name,
            "last_renewed": str(s.last_renewed_date),
            "auto_renew": s.auto_renew,
            "amount": s.amount
        })

    return result