from src.logger import log_question


def test_log_question_creates_log_file(tmp_path):
    test_log_file = tmp_path / "test_questions_log.csv"

    log_question(
        user_question="How long does delivery take?",
        category="Shipping",
        status="answered",
        log_file_path=test_log_file
    )

    assert test_log_file.exists()

    content = test_log_file.read_text(encoding="utf-8")

    assert "timestamp,user_question,matched_category,status" in content
    assert "How long does delivery take?" in content
    assert "Shipping" in content
    assert "answered" in content