import math


def get_range_for_difficulty(difficulty: str):
    """Return the inclusive guessing range for a named difficulty.

    Args:
        difficulty: Difficulty label selected by the player.

    Returns:
        A two-item tuple containing the inclusive lower and upper bounds
        for the selected difficulty. Unknown difficulty values fall back
        to the Normal range.
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
    return 1, 50

# ERROR: I am unable to round guesses
# FIX: changed so that all floats are now rounded instead of floored and all strings are stripped prior to converting to integer, using GitHub Copilot.
def parse_guess(raw: str):
    """Validate and convert raw user input into an integer guess.

    The parser accepts standard integers as well as decimal and scientific
    notation inputs. Floating-point values are rounded to the nearest integer.
    Empty input, non-numeric input, and non-finite numeric values are rejected.

    Args:
        raw: Raw text entered by the player.

    Returns:
        A tuple of ``(is_valid, parsed_value, error_message)``. When parsing
        succeeds, ``is_valid`` is ``True``, ``parsed_value`` is the integer
        guess, and ``error_message`` is ``None``. When parsing fails,
        ``is_valid`` is ``False``, ``parsed_value`` is ``None``, and
        ``error_message`` contains a user-facing validation message.
    """
    if raw is None:
        return False, None, "Enter a guess."

    raw = raw.strip()

    if raw == "":
        return False, None, "Enter a guess."

    try:
        # Accept decimal/scientific notation while rejecting inf/nan values.
        if any(marker in raw for marker in (".", "e", "E")):
            number = float(raw)
            if not math.isfinite(number):
                raise ValueError("non-finite number")
            value = round(number)
        else:
            value = int(raw)
    except (TypeError, ValueError, OverflowError):
        return False, None, "That is not a number."

    return True, value, None

# ERROR: The hints for the guesses are off.
# FIX: Fixes general logic within the solution. Solved using pointers from Claude and by myself. 
def check_guess(guess, secret):
    """Compare a guess against the secret value and return gameplay feedback.

    The function attempts numeric comparison first so numeric strings can be
    handled safely. If numeric conversion is not possible, values are compared
    as strings.

    Args:
        guess: The player's submitted guess.
        secret: The secret target value for the current game.

    Returns:
        A tuple of ``(outcome, message)`` where ``outcome`` is one of
        ``"Win"``, ``"Too High"``, or ``"Too Low"``, and ``message`` is the
        corresponding user-facing hint.
    """
    try:
        guess_value = int(guess)
        secret_value = int(secret)
    except (TypeError, ValueError):
        guess_value = str(guess)
        secret_value = str(secret)

    if guess_value == secret_value:
        return "Win", "🎉 Correct!"

    if guess_value > secret_value:
        return "Too High", "📈 Go LOWER!" # Should be LOWER
    return "Too Low", "📉 Go HIGHER!" # Should be HIGHER

# ERROR: Score updates are inaccurate.
# FIX: Made every incorrect guess be a penalty, no matter the outcome, using GitHub CoPilot. I also made sure that the minimum score was always 10.
def update_score(current_score: int, outcome: str, attempt_number: int):
    """Calculate the updated score after a guess outcome.

    Winning awards a decreasing bonus based on the attempt number, with a
    minimum win bonus of 10 points. Incorrect numeric guesses apply a fixed
    penalty. Any other outcome leaves the score unchanged.

    Args:
        current_score: Score before applying the latest result.
        outcome: Result label returned from ``check_guess``.
        attempt_number: One-based attempt index for the current round.

    Returns:
        The new score after applying the win bonus or penalty.
    """
    if outcome == "Win":
        safe_attempt = max(attempt_number, 1)
        points = max(100 - 10 * (safe_attempt - 1), 10)
        return current_score + points

    if outcome in ("Too High", "Too Low"):
        return current_score - 5

    return current_score


def update_high_score(current_high_score: int, current_score: int):
    """Return the higher of the existing high score and current score.

    Negative or missing score values are normalized to zero so the stored high
    score always remains a non-negative integer.

    Args:
        current_high_score: Best score recorded so far.
        current_score: Score produced by the current game state.

    Returns:
        The score value that should be stored as the high score.
    """
    safe_high_score = max(current_high_score or 0, 0)
    safe_current_score = max(current_score or 0, 0)
    return max(safe_high_score, safe_current_score)
