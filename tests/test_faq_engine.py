from src.faq_engine import find_best_answer, load_faq_data


def test_faq_data_loads_successfully():
    faq_data = load_faq_data()

    assert "faqs" in faq_data
    assert len(faq_data["faqs"]) >= 20


def test_known_shipping_question_gets_answered():
    result = find_best_answer("How long does delivery take?")

    assert result["status"] == "answered"
    assert result["category"] == "Shipping"
    assert "3-5 business days" in result["answer"]


def test_unknown_question_uses_fallback():
    result = find_best_answer("Do you sell perfumes?")

    assert result["status"] == "fallback"
    assert result["category"] == "Fallback"
    assert "contact Urban Threads Co. support" in result["answer"]


def test_empty_question_uses_fallback():
    result = find_best_answer("")

    assert result["status"] == "fallback"
    assert result["category"] == "Fallback"