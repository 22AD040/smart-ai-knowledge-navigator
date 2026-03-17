from utils.embedding_utils import get_embedding
from sklearn.metrics.pairwise import cosine_similarity

def similarity(a,b):

    emb1=get_embedding(a)
    emb2=get_embedding(b)

    score=cosine_similarity([emb1],[emb2])[0][0]

    return score