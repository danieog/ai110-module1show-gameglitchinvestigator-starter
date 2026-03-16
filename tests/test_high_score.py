from logic_utils import update_high_score


def test_update_high_score_keeps_existing_best_score():
    updated = update_high_score(current_high_score=85, current_score=70)

    assert updated == 85


def test_update_high_score_replaces_best_score_when_higher():
    updated = update_high_score(current_high_score=85, current_score=95)

    assert updated == 95