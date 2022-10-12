from collections import Counter

from app.services.words import WordsService


def test_default_count_words():
    words_service = WordsService()
    assert words_service.words_counter == Counter()


def test_count_words():
    words_service = WordsService()
    words = [
        "ball",
        "ball",
        "ball",
        "ball",
        "hello",
        "hello",
        "eggs",
        "eggs",
        "pool",
        "pool",
        "wild",
        "daily",
        "-1",
        "True",
    ]
    local_words_counter = Counter()
    for _ in range(20):
        words_service.count_words(words)
        local_words_counter += Counter(words)
        assert words_service.words_counter == local_words_counter


def test_frequency_rank():
    words_service = WordsService()
    words_service.count_words(
        [
            "ball",
            "ball",
            "ball",
            "ball",
            "ball",
            "eggs",
            "eggs",
            "eggs",
            "pool",
            "pool",
            "pool",
            "wild",
            "daily",
        ]
    )
    assert words_service.frequency_rank() == {
        "ball": 5,
        "eggs": 3,
        "pool": 3,
        "wild": 1,
        "daily": 1,
    }


def test_frequency_rank_default():
    words_service = WordsService()
    assert words_service.frequency_rank() is None
