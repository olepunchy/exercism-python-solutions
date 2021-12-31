"""High Scores from Exercism"""


def latest(scores):
    """
    Return the last score in the scores list.

    param: list of scores
    return: last score in scores
    """
    return scores[-1]


def personal_best(scores):
    """
    Return the highest score in scores.

    param: list of scores
    return: highest score in scores

    """
    return max(scores)


def personal_top_three(scores):
    """
    Return the top three scores from scores.

    If there are fewer than three scores, return the scores.

    param: list of scores
    return: highest three scores from scores.
    """
    # Sort the scores in descending order
    scores.sort(reverse=True)

    if len(scores) < 3:
        return scores

    # Return the first three
    return [scores[0], scores[1], scores[2]]
