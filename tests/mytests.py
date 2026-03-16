import pytest

from logic_utils import check_guess, get_range_for_difficulty


@pytest.mark.parametrize(
    "guess, expected_outcome",
    [
        (1, "Too Low"),
        (19, "Too Low"),
        (45, "Win"),
        (86, "Too High"),
    ],
)
def test_check_guess_hard_difficulty_specific_guesses(guess, expected_outcome):
    low, high = get_range_for_difficulty("Hard")
    assert (low, high) == (1, 100)

    secret = 45
    outcome, _message = check_guess(guess, secret)
    assert outcome == expected_outcome
