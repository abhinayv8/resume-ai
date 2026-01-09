from typing import List, Dict
from collections import Counter

def generate_hiring_analytics(ranked_candidates: List[Dict]) -> Dict:
    skill_gap_counter = Counter()
    avg_score = 0

    for candidate in ranked_candidates:
        avg_score += candidate["final_score"]
        skill_gap_counter.update(candidate["missing_skills"])

    avg_score = round(avg_score / len(ranked_candidates), 2) if ranked_candidates else 0

    return {
        "average_match_score": avg_score,
        "most_common_missing_skills": skill_gap_counter.most_common(5),
        "total_candidates": len(ranked_candidates)
    }

