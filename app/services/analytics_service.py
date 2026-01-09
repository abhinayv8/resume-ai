def generate_hiring_analytics(ranked):
    avg = sum(r["score"] for r in ranked) / len(ranked) if ranked else 0
    return {"average_score": round(avg, 2)}
