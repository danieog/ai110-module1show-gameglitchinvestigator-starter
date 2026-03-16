from logic_utils import check_guess, parse_guess, update_score


def test_parse_guess_handles_overflow_float_input_gracefully():
    """Very large scientific float input should not crash parsing."""
    ok, value, err = parse_guess("1.0e309")

    assert ok is False
    assert value is None
    assert err == "That is not a number."


def test_check_guess_accepts_numeric_string_guess_without_crashing():
    """A numeric string guess should be handled safely against int secrets."""
    outcome, message = check_guess("9", 10)

    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_update_score_caps_win_points_when_attempt_number_is_zero():
    """Invalid attempt_number=0 should not award more than max win points."""
    updated = update_score(current_score=0, outcome="Win", attempt_number=0)

    assert updated == 100
