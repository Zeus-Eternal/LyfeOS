from sentence_transformers import SentenceTransformer
import json
import sys

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def embed(text: str):
    vec = model.encode(text).tolist()
    return vec

if __name__ == '__main__':
    text = " ".join(sys.argv[1:])
    vec = embed(text)
    json.dump({'embedding': vec}, sys.stdout)
