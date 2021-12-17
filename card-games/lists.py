"""Card Games - Exercism Python Exercises"""


def get_rounds(number):
    """

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1, rounds_2):
    """

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    rounds = rounds_1[:]
    for go_round in rounds_2:
        rounds.append(go_round)
    return rounds


def list_contains_round(rounds, number):
    """

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    """
    if number in rounds:
        return True

    return False


def card_average(hand):
    """

    :param hand: list - cards in hand.
    :return:  float - average value of the cards in the hand.
    """
    total = 0
    for card in hand:
        total += card

    return total / len(hand)


def approx_average_is_average(hand):
    """

    :param hand: list - cards in hand.
    :return: bool - if approximate average equals to the `true average`.
    """
    end_average = (hand[0] + hand[-1]) / 2
    mid_index = len(hand) // 2
    mid_average = float(hand[mid_index])

    hand_sum = 0
    for card in hand:
        hand_sum += card

    true_average = hand_sum / len(hand)

    return end_average == true_average or mid_average == true_average


def average_even_is_average_odd(hand):
    """

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    even_count = 0
    even_average = 0
    even_sum = 0

    for i in range(0, len(hand), 2):
        even_count += 1
        even_sum += hand[i]

    even_average = even_sum / even_count

    odd_count = 0
    odd_average = 0
    odd_sum = 0

    for i in range(1, len(hand), 2):
        odd_count += 1
        odd_sum += hand[i]

    odd_average = odd_sum / odd_count

    return even_average == odd_average


def maybe_double_last(hand):
    """

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    if hand[-1] == 11:
        new_hand = hand[:]
        new_hand[-1] = 22
        return new_hand

    return hand
