import json
from embed import generate_embeddings
from store import save_embeddings
from query import search

# Load processed logs
with open("../data/processed_logs.json") as f:
    logs = json.load(f)

# Generate embeddings
embeddings = generate_embeddings(logs)

# Save embeddings
save_embeddings(embeddings, logs, "../data/embeddings.json")

# Load embeddings
with open("../data/embeddings.json") as f:
    data = json.load(f)

# Search
results = search("database error", data)

for score, log in results:
    print(score, log)
print("\nShowing first 3 embeddings:\n")

for item in data[:3]:
    print("LOG:", item["log"]["message"])
    print("VECTOR (first 5 values):", item["embedding"][:5])
    print("-" * 50)
