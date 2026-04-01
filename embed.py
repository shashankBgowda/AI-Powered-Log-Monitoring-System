from sentence_transformers import SentenceTransformer
import numpy as np
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load model once
model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embeddings(logs, save=False):
    """
    Generate embeddings from log messages.

    Args:
        logs (list): List of log dictionaries
        save (bool): Save embeddings to file

    Returns:
        np.ndarray: Embedding vectors
    """

    try:
        logging.info("Generating embeddings...")

        # 🔥 Extract only messages (IMPORTANT FIX)
        messages = [log["message"] for log in logs]

        embeddings = model.encode(messages)

        # Debug logs
        logging.info(f"Total embeddings generated: {len(embeddings)}")
        logging.info(f"Vector shape: {embeddings.shape}")

        # Print sample vectors
        for i, vec in enumerate(embeddings[:2]):
            print(f"\nSample Vector {i}: {vec[:10]}...")

        # Save if needed
        if save:
            np.save("vectors.npy", embeddings)
            logging.info("Embeddings saved to vectors.npy")

        return embeddings

    except Exception as e:
        logging.error(f"Error generating embeddings: {str(e)}")
        raise