from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def rank_resumes(resumes, job_text):
    texts = resumes + [job_text]
    vectors = TfidfVectorizer().fit_transform(texts)
    scores = cosine_similarity(vectors[:-1], vectors[-1:]).flatten()

    return [
        {"resume_id": i + 1, "score": float(score)}
        for i, score in enumerate(scores)
    ]

