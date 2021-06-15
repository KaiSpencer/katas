def spin_words(words: str) -> str:
    return " ".join([word[::-1] if len(word) > 4 else word for word in words.split(" ")])
