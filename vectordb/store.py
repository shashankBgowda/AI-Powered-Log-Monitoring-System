import json


def save_embeddings(embeddings, logs, output_file):
    data = []

    for i in range(len(logs)):
        data.append({"log": logs[i], "embedding": embeddings[i].tolist()})

    with open(output_file, "w") as f:
        json.dump(data, f, indent=4)
