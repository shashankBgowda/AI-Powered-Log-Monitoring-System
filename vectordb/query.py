from sentence_transformers import SentenceTransformer
import numpy as np
import json

model = SentenceTransformer("all-MiniLM-L6-v2")


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def search(query, data):
    query_embedding = model.encode([query])[0]

    results = []

    for item in data:
        score = cosine_similarity(query_embedding, item["embedding"])
        results.append((score, item["log"]))

    results.sort(reverse=True, key=lambda x: x[0])

    return results[:3]
