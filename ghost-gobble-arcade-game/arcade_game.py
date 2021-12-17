""" Exercism challenge - Ghost Gobble Arcade Game"""

def eat_ghost(power_pellet_active, touching_ghost):
    """

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost:  bool - is the player touching a ghost?
    :return: bool
    """
    return power_pellet_active and touching_ghost


def score(touching_power_pellet, touching_dot):
    """

    :param touching_power_pellet: bool - does the player have an active power pellet?
    :param touching_dot:  bool - is the player touching a dot?
    :return: bool
    """
    return touching_power_pellet or touching_dot


def lose(power_pellet_active, touching_ghost):
    """

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool
    """
    # return power_pellet_active and touching_ghost
    if power_pellet_active:
        return False

    return touching_ghost


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """

    :param has_eaten_all_dots: bool - has the player "eaten" all the dots?
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost:  bool - is the player touching a ghost?
    :return: bool
    """
    won = False
    if has_eaten_all_dots and touching_ghost and power_pellet_active:
        won = True
    elif has_eaten_all_dots and touching_ghost:
        won = False
    elif has_eaten_all_dots:
        won = True
    else:
        won = False

    return won
