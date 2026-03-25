import json
import os


def save_logs(logs, output_path):
    """Save structured logs to a JSON file."""
    os.makedirs(
        os.path.dirname(output_path), exist_ok=True
    )  # auto-create Output/ folder

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(logs, file, indent=4)

    print(f"  [Saved] {output_path}")
