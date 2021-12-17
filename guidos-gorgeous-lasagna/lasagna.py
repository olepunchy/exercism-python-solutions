"""
Exercism Python Basics problem for doing simple calculations on cooking lasagna.
"""
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(minutes):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - minutes

def preparation_time_in_minutes(layers):
    """ Calculate the total preparation time based on the number of layers.

    :param layers: int number of layers for the lasagna.
    :return: the time in minutes result of PREPARATION_TIME * layers
    """
    return PREPARATION_TIME * layers

def elapsed_time_in_minutes(layers, elapsed_time):
    """
    Calculate the total time needed to bake the lasagna.

    :param layers: int the number of layers for the lasagna.
    :elapsed_time: int the number of minutes the lasagna has been cooking.
    :return: the total number of minutes spent on the lasagna.
    """
    prep_time = preparation_time_in_minutes(layers)
    return prep_time + elapsed_time
