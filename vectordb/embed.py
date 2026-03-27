from sentence_transformers import SentenceTransformer

# Load pre-trained model
model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embeddings(logs):
    messages = [log["message"] for log in logs]
    embeddings = model.encode(messages)

    return embeddings
