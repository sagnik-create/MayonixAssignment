import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def get_top_k_similar(query_embedding, message_embeddings, messages, k=3):
    similarities = cosine_similarity(query_embedding, message_embeddings)[0]

    ranked_indices = np.argsort(similarities)[::-1][:k]

    results = []
    for idx in ranked_indices:
        results.append({
            "message": messages[idx],
            "score": float(similarities[idx])
        })

    return results
