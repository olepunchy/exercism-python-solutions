"""Raindrops from Exercism"""


def convert(number):
    """
    Convert a number to a string of raindrop sounds.

    param: int number
    return: str formatted string based on input
    """
    if number % 7 == 0 and number % 5 == 0 and number % 3 == 0:
        return "PlingPlangPlong"

    if number % 7 == 0 and number % 5 == 0:
        return "PlangPlong"

    if number % 7 == 0 and number % 3 == 0:
        return "PlingPlong"

    if number % 5 == 0 and number % 3 == 0:
        return "PlingPlang"

    if number % 7 == 0:
        return "Plong"

    if number % 5 == 0:
        return "Plang"

    if number % 3 == 0:
        return "Pling"

    return str(number)
