from collections import Counter


def test_get_words_route_default(test_app):
    response = test_app.get("/api/v1/words")
    assert response.status_code == 200
    assert response.json() == {}


def test_add_words_route(test_app):
    response = test_app.post(
        "/api/v1/words",
        json={"value": "ball,ball,ball,ball,eggs,eggs,pool,pool,wild,daily"},
    )
    assert response.status_code == 200

    response = test_app.get("/api/v1/words")
    assert response.status_code == 200
    assert response.json() == Counter(
        [
            "ball",
            "ball",
            "ball",
            "ball",
            "eggs",
            "eggs",
            "pool",
            "pool",
            "wild",
            "daily",
        ]
    )


def test_frequency_distribution_rank_route(test_app):
    response = test_app.get("/api/v1/words/frequency_distribution_rank")
    assert response.status_code == 200
    assert response.json() == {
        "ball": 5,
        "eggs": 2,
        "pool": 2,
        "wild": 1,
        "daily": 1,
    }
