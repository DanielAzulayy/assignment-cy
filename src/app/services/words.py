from collections import Counter
from typing import List

from app.utils.words import calculate_frequency_rank


class WordsService:
    def __init__(self):
        self._words_counter: dict = Counter()

    @property
    def words_counter(self):
        return self._words_counter

    def count_words(self, parsed_words: List[str]):
        self._words_counter += Counter(parsed_words)

    def frequency_rank(self):
        if len(self._words_counter) == 0:
            return None

        five_most_common = self._words_counter.most_common()[:5]
        _, most_common_count = five_most_common[0]
        _, least_common_count = five_most_common[-1]

        return {
            word: calculate_frequency_rank(
                word_count, least_common_count, most_common_count
            )
            for word, word_count in five_most_common
        }
