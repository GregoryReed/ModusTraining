

def get_candies(candies: list) -> int:
    """
    Get the amount of unique candies someone would receive if
        the list of candies are split between 2 people
    :param candies: a list of candies to be shared
    :return: the max amount of unique candies someone would recive
    """
    return min(len(set(candies)), int(len(candies)/2))
