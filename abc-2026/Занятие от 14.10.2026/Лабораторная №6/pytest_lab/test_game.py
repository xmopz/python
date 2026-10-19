
from unittest.mock import patch

import game


def test_create_game():
    with patch("game.random.choice", return_value="and"):
        result = game.create_game()

    assert result["secret"] == "and"
    assert result["mask"] == ["*", "*", "*"]
    assert result["hp"] == 3


def test_correct_letter():
    state = {
        "secret": "and",
        "mask": ["*", "*", "*"],
        "known_letter": set(),
        "hp": 3,
        "game_status": True,
    }

    game.check_letter(state, "a")

    assert state["mask"] == ["a", "*", "*"]
    assert state["hp"] == 3


def test_wrong_letter():
    state = {
        "secret": "and",
        "mask": ["*", "*", "*"],
        "known_letter": set(),
        "hp": 3,
        "game_status": True,
    }

    game.check_letter(state, "z")

    assert state["hp"] == 2
