import faiss
import numpy as np
from utils.embedding_utils import get_embedding
from sklearn.metrics.pairwise import cosine_similarity

dimension = 384

index = faiss.IndexFlatL2(dimension)

documents = []


def add_document(text):

    emb = get_embedding(text)

    index.add(np.array([emb]).astype("float32"))

    documents.append(text)


def search(query, top_k=5):

    if len(documents) == 0:
        return []

    query_emb = get_embedding(query)

    D, I = index.search(np.array([query_emb]).astype("float32"), top_k)

    results = []

    for idx in I[0]:

        doc = documents[idx]

        doc_emb = get_embedding(doc)

        score = cosine_similarity([query_emb], [doc_emb])[0][0]

        snippet = doc[:300]

        results.append({
            "text": snippet,
            "score": round(float(score), 3)
        })

    return results