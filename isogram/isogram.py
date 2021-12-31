"""Isogram from Exercism"""


def is_isogram(string):
    """
    Determine if the input string is an isogram.

    param: str to test for beign an isogram
    return: True or False if the input is an isogram
    """
    # An empty string is an isogram
    if string == "":
        return True

    # Lowercase the string to simplify comparisions
    input = str.lower(string)

    # Dictionary to hold the letters we've seen
    used_letters = {}

    for letter in input:
        # Only testing alpha characters, all others are ignored, e.g. hyphen
        if letter.isalpha():
            # If the letter has already been seen, return False
            if letter in used_letters:
                return False

            # Otherwise, add it to the letters we've seen
            used_letters[letter] = 1

    # Did not find a repeat of the alpha characters in the input
    return True
