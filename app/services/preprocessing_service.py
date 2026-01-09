import re

def preprocess_text(text: str) -> str:
    """
    Clean and normalize raw resume text.
    """
    text = normalize_whitespace(text)
    text = normalize_case(text)
    text = remove_non_informative_chars(text)
    return text.strip()

def normalize_whitespace(text: str) -> str:
    # Replace multiple spaces with one
    text = re.sub(r"[ \t]+", " ", text)

    # Normalize line breaks
    text = re.sub(r"\n{2,}", "\n", text)

    return text

def normalize_case(text: str) -> str:
    return text.lower()

def remove_non_informative_chars(text: str) -> str:
    # Remove weird bullet characters and symbols
    text = re.sub(r"[•●■►]", "", text)

    # Remove repeated punctuation
    text = re.sub(r"[.,]{2,}", ".", text)

    return text
