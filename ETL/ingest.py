import os


def read_logs(file_path):
    """Read all lines from a single log file."""
    logs = []
    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        for line in file:
            logs.append(line.strip())
    return logs


def read_all_logs(folder_path):
    """Loop through all log files in Raw_data_logs folder."""
    all_logs = {}

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        if os.path.isfile(file_path):
            print(f"  [Ingesting] {file_name}")
            all_logs[file_name] = read_logs(file_path)

    return all_logs  # { "Application_logs": [...lines], "Docker_logs": [...] }
