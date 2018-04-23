

def volume_of_water(island_heights: list) -> int:
    """
    Calculate the volume of water 
    in a 2 dimensional representation of an island
    :param island_heights: A list of island heights in a 2 dimensional list
    :return: the total depth of all the lakes of an island
    """
    total = 0
    # Get the highest point and the starting point of the island
    cu_max = island_heights[0]
    total_peak = island_heights.index(max(island_heights))

    # Get all the depths between the starting point and the first peak
    for location in range(len(island_heights[:total_peak])):
        point = island_heights[location]
        # If the current location is greater or equal
        # To the highest point between the current point and the edge,
        # All the water would run off the edge
        if point >= cu_max:
            cu_max = point
        total += cu_max - point

    # Get all the depths from the edge and the original peak
    cu_max = island_heights[-1]
    for location in range(len(island_heights)-1, total_peak, -1):
        point = island_heights[location]
        # If the current location is greater or equal
        # To the highest point between the current point and the edge,
        # All the water would run off the edge
        if point >= cu_max:
            cu_max = point
        total += cu_max - point
    return total
