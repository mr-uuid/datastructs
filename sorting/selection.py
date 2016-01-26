def sort(array):
    """
    Algorithm:
    1. Takes the array and finds the min:
        [2, 3, 1, 5, 4] -> min = 1
         ^ Start here
    2. Swaps the beginning array with the min:
        [1, 3, 2, 5, 4]
         ^     ^
    3. Repeat with the rest of the array:
        [1, 3, 2, 5, 4]
            ^ Start here

    This algorithm takes O(n^2) time worst case and O(n) best case.
    """

    for starting_index, starting_value in enumerate(array):
        _min = (starting_index, starting_value)
        inner_counter = starting_index
        # Itertate the inner loop and determine the minimum
        for inner_val in array[inner_counter:]:
            if inner_val < _min[1]:
                _min = (inner_counter, inner_val)
            inner_counter += 1
        # Swap the min with the starting index
        array[starting_index], array[_min[0]] = array[_min[0]], starting_value
    return array

if __name__ == "__main__":
    array = lambda: list("The quick brown fox jumps over the lazy dog".replace(" ","").lower())
    print sort(array())
