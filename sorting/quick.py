def sort(array, first=None, last=None):
    """
    Algorithm:
    1. Takes the array and breaks it down into smaller arrays:
        [3, 5, 2, 1, 4]
        [3, 5, 2, 1, 4] pivot = 4
        [3, 5, 2, 1, 4]
         i        j     Start two counters, that move in opposite directions,
        [3, 5, 2, 1, 4]
            i     j     Move first counter until you reach an element > pivot
        Then start moving J until its at an element less than the pivot, or unil it reaches i.
        If you find an element with j, swap. Else,

    It does the max number of comparisons when the array is sorted - (n-1)n/2 ~= n^2
    """

    first = first if first is not None else 0
    last = last if last is not None else len(array) - 1

    # Base case for an array of 0 or 1 items
    if len(array) <= 1 or last - first < 1:
        return array

    i, j = first, last - 1
    pivot = array[last]

    # Start at beginning of array and determine if there is any value before the pivot
    # that is greator then the pivot that should be put after the pivot
    while i <= j:
        # Skip all values that are less then the pivot
        if array[i] <= pivot:
            i += 1
        else:
            # Stop when two less then and greator than partitions meet
            if i >= j: break
            # Increment greator than partition until we can get a valid swap
            while j >= i:
                if array[j] >= pivot:
                    j -= 1
                else:
                    # When a value that is less than the pivot in the greator than partition is found, swap it
                    array[i], array[j] = array[j], array[i]
                    break

    # Place the pivot in the right place
    array[last], array[i] = array[i], array[last]
    # Sort the partitions
    sort(array, first, i-1)
    sort(array, i+1, last)
    return array

if __name__ == "__main__":
    array = lambda: list("The quick brown fox jumps over the lazy dog".replace(" ","").lower())
    array = lambda: [3, 1, 5]
    print sort(array())
