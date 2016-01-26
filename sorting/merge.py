def sort(array):
    """
    Algorithm:
    1. Takes the array and breaks it down into smaller arrays:
        [3, 1, 2]    | [5, 4]
        [3, 1] | [2] | [5, 4]
    2. Then the algorithm begins sorting and merging the small, 1x1 arays:
        [1, 3] | [2] | [5, 4]
        [1, 2, 3] | [5, 4]
        [1, 2, 3] | [4, 5]
        [1]
        [1, 2]
        [1, 2, 3]
        [1, 2, 3, 4]
        [1, 2, 3, 4, 5]

    This algorithm takes O(n*ln(n)) for all casses, and needs N space.
    """

    def merge(a1, a2):
        result = []
        while len(a1) or len(a2):
            if a1 == [] or a2 == []:
                result.extend(a1)
                result.extend(a2)
                break
            if a1[0] <= a2[0]:
                result.append(a1.pop(0))
            else:
                result.append(a2.pop(0))
        return result

    length = len(array)
    if length > 1:
        return merge(sort(array[:length/2]), sort(array[length/2:]))
    return array

if __name__ == "__main__":
    array = lambda: list("The quick brown fox jumps over the lazy dog".replace(" ","").lower())
    print sort(array())
