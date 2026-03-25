import os
from ingest import read_all_logs
from transform import transform_logs
from load import save_logs


def run_pipeline():
    # ── Paths ──────────────────────────────────────────────────────────────────
    base_path = r"C:\Users\Shashank B G\OneDrive\Desktop\Devops+AI_Project"
    raw_folder = os.path.join(base_path, "Raw_data_logs")  # INPUT  folder
    output_folder = os.path.join(base_path, "Output")  # OUTPUT folder

    print("=" * 50)
    print("   DevOps+AI Log Pipeline Starting...")
    print("=" * 50)

    # ── Step 1: Ingest all log files ───────────────────────────────────────────
    print("\n[STEP 1] Ingesting logs...")
    all_logs = read_all_logs(raw_folder)

    # ── Step 2 & 3: Transform + Save each log file separately ─────────────────
    print("\n[STEP 2 & 3] Transforming and Saving...")
    total_parsed = 0

    for file_name, raw_lines in all_logs.items():
        structured = transform_logs(raw_lines)
        total_parsed += len(structured)

        # Each log file gets its own output JSON
        # e.g. Application_logs → Output/Application_logs.json
        output_path = os.path.join(output_folder, f"{file_name}.json")
        save_logs(structured, output_path)

    # ── Done ───────────────────────────────────────────────────────────────────
    print("\n" + "=" * 50)
    print(f"  Pipeline Completed!")
    print(f"  Files processed : {len(all_logs)}")
    print(f"  Total log lines : {total_parsed}")
    print(f"  Output folder   : {output_folder}")
    print("=" * 50)


if __name__ == "__main__":
    run_pipeline()
