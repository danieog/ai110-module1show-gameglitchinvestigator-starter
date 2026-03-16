import math


def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
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
    if outcome == "Win":
        safe_attempt = max(attempt_number, 1)
        points = max(100 - 10 * (safe_attempt - 1), 10)
        return current_score + points

    if outcome in ("Too High", "Too Low"):
        return current_score - 5

    return current_score


def update_high_score(current_high_score: int, current_score: int):
    safe_high_score = max(current_high_score or 0, 0)
    safe_current_score = max(current_score or 0, 0)
    return max(safe_high_score, safe_current_score)
