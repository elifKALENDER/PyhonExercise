"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    return ([number, number + 1, number + 2])


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return (rounds_1 + rounds_2)


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    return number in rounds


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    return (sum(hand) / len(hand))


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    mid_value = card_average(hand)
    if mid_value == (hand[0] + hand[-1]) / 2 or mid_value == hand[len(hand) // 2]:
        return True
    else:
        return False


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    even_sum = 0
    odd_sum = 0
    # even_array=[]
    # odd_array=[]
    even_count = 0
    odd_count = 0
    average_even = 0
    average_odd = 0
    for i, number in enumerate(hand):
        if i % 2 == 1:
            odd_sum += number
            # odd_array.append(hand[i])
            # average_odd=odd_sum/len(odd_array)
            odd_count += 1
            average_odd = odd_sum / odd_count

        else:
            even_sum += number
            # even_array.append(hand[i])
            # average_even=even_sum/len(even_array)
            even_count += 1
            average_even = even_sum / even_count
    return (average_odd == average_even)


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if hand[-1] == 11:
        hand[-1] = 22
        return (hand)
    else:
        return (hand)
