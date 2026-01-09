def hybrid_score(skill_score: float, semantic_score: float) -> float:
    """
    Weighted hybrid score:
    - Skills: 60%
    - Semantics: 40%
    """
    final_score = (0.6 * skill_score) + (0.4 * semantic_score)
    return round(final_score, 2)
