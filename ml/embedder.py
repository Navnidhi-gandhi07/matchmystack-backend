from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text: str):
    if not text:
        return [0.0]*768
    return model.encode(text).tolist()
