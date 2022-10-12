from app.utils import words as words_utils


def test_parse_words():
    assert words_utils.parse_words("") == []

    assert words_utils.parse_words(",,a,a,s,asdasdasd,,asds,") == list(
        filter(None, ",,a,a,s,asdasdasd,,asds,".split(","))
    )

    assert words_utils.parse_words(",[]];,...]],s,asdasdasd,,asds,") == list(
        filter(None, ",[]];,...]],s,asdasdasd,,asds,".split(","))
    )


def test_frequency_rank():
    assert words_utils.calculate_frequency_rank(4, 1, 4) == 5
    assert words_utils.calculate_frequency_rank(4, 4, 4) == 5
    assert words_utils.calculate_frequency_rank(0, 0, 0) == 0
    assert words_utils.calculate_frequency_rank(0, 1, 1) == 0
