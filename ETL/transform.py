import re


def parse_log(log):
    """Parse a single log line into structured dict."""
    pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)"
    match = re.match(pattern, log)

    if match:
        return {
            "timestamp": match.group(1),
            "level": match.group(2),
            "message": match.group(3),
        }
    return None  # skip lines that don't match the pattern


def transform_logs(logs):
    """Transform a list of raw log strings into structured dicts."""
    structured_logs = []

    for log in logs:
        parsed = parse_log(log)
        if parsed:
            structured_logs.append(parsed)

    return structured_logs
