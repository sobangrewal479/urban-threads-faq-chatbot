import csv
from datetime import datetime
from pathlib import Path


LOG_FILE_PATH = Path("logs/questions_log.csv")


def log_question(user_question, category, status, log_file_path=LOG_FILE_PATH):
    """
    Save the customer's question to a CSV log file.
    """

    log_file_path.parent.mkdir(parents=True, exist_ok=True)

    file_exists = log_file_path.exists()

    with open(log_file_path, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["timestamp", "user_question", "matched_category", "status"])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            user_question,
            category,
            status
        ])