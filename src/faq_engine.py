import json
import string
from pathlib import Path


FAQ_FILE_PATH = Path("data/faqs.json")

STOP_WORDS = {
    "a", "an", "and", "are", "at", "be", "by", "can", "do", "does",
    "for", "from", "how", "i", "if", "in", "is", "it", "my", "of",
    "on", "or", "the", "to", "what", "when", "where", "with", "you",
    "your", "we"
}


def load_faq_data(file_path=FAQ_FILE_PATH):
    """
    Load FAQ data from the JSON file.
    """

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data


def clean_text(text):
    """
    Make text easier to compare:
    - lowercase
    - remove punctuation
    - remove extra spaces
    """

    if not text:
        return ""

    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = " ".join(text.split())

    return text


def get_meaningful_words(text):
    """
    Keep only useful words for matching.
    This removes common words like 'do', 'you', 'the', etc.
    """

    cleaned_text = clean_text(text)
    words = cleaned_text.split()

    meaningful_words = {
        word for word in words
        if word not in STOP_WORDS and len(word) > 2
    }

    return meaningful_words


def calculate_match_score(user_question, faq_item):
    """
    Calculate a simple score between the user's question and one FAQ item.
    Higher score means better match.
    """

    cleaned_user_question = clean_text(user_question)
    cleaned_faq_question = clean_text(faq_item.get("question", ""))

    if not cleaned_user_question:
        return 0

    score = 0

    # Keyword matching is the strongest signal.
    keywords = faq_item.get("keywords", [])

    for keyword in keywords:
        cleaned_keyword = clean_text(keyword)

        if cleaned_keyword and cleaned_keyword in cleaned_user_question:
            score += 4

    # Match meaningful words only.
    user_words = get_meaningful_words(user_question)
    faq_words = get_meaningful_words(faq_item.get("question", ""))

    common_words = user_words.intersection(faq_words)

    score += len(common_words)

    return score


def find_best_answer(user_question, faq_data=None):
    """
    Find the best FAQ answer for the user's question.
    If no good match is found, return fallback answer.
    """

    if faq_data is None:
        faq_data = load_faq_data()

    fallback_answer = faq_data["fallback"]["answer"]
    faqs = faq_data["faqs"]

    best_match = None
    best_score = 0

    for faq_item in faqs:
        score = calculate_match_score(user_question, faq_item)

        if score > best_score:
            best_score = score
            best_match = faq_item

    # Minimum score required to trust the answer.
    # This prevents weak matches like "Do you sell perfumes?"
    minimum_score = 3

    if best_match and best_score >= minimum_score:
        return {
            "answer": best_match["answer"],
            "category": best_match["category"],
            "status": "answered",
            "score": best_score
        }

    return {
        "answer": fallback_answer,
        "category": "Fallback",
        "status": "fallback",
        "score": best_score
    }