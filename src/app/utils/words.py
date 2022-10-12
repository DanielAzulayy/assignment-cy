from decimal import DivisionByZero
from functools import lru_cache
from typing import List


def parse_words(words: str) -> List[str]:
    return list(filter(None, words.split(",")))


@lru_cache
def calculate_frequency_rank(
    current_word_count, least_common_count, most_common_count
) -> int:
    try:
        if 0 in [current_word_count, least_common_count, most_common_count]:
            return 0

        word_count_minus_least_count = current_word_count - least_common_count
        most_minus_least_count = most_common_count - least_common_count

        division_result = word_count_minus_least_count / most_minus_least_count

        return int((4 * division_result) + 1)
    except ZeroDivisionError:
        return 5
