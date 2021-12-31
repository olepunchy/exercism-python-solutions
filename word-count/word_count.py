"""Word Count from Exercism"""


def count_words(sentence):
    """
    Count the number of words in a sentence.

    param: str the sentence to count words
    return: dictionary of word (str) keys and count (int) values
    """
    input = str.lower(sentence)

    special_characters = [
        "!",
        "@",
        "#",
        "$",
        "%",
        "^",
        "&",
        "*",
        "(",
        ")",
        ":",
        ",",
        ".",
        "_",
        "\n",
    ]

    for character in special_characters:
        input = input.replace(character, " ")

    words = input.split()

    words_dict = {}

    for word in words:

        word = word.lstrip("'")
        word = word.rstrip("'")

        if word in words_dict:
            words_dict[word] += 1

        else:
            words_dict[word] = 1

    return words_dict
