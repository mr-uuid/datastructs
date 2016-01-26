def sort(array):
    """
    Algorithm:
    1. Start at the beginning of the array:
        [5, 4, 3, 2, 1] -> min = 1
         ^ Start here
    2. Check if there are elements to the left of the current item that are less then the selected element:
        If there isnt, go on to the next element. If there is, shift that element left, and re run the check:
        [5, 4, 3, 2, 1]
            ^
        [5,  , 3, 2, 1] 4
            ^
        [ , 5, 3, 2, 1] 4
            ^
        [4, 5, 3, 2, 1]
         ^
    3. Repeat ...
        [4, 5, 3, 2, 1]
               ^
        [4, 5,  , 2, 1] 3
               ^
        [4, 5,  , 2, 1] 3
            ^
        [4,  , 5, 2, 1] 3
               ^
        [4,  , 5, 2, 1] 3
            ^
        [ , 4, 5, 2, 1] 3
            ^
        [3, 4, 5, 2, 1]
         ^
    4. Repeat ...
        [3, 4, 5, 2, 1]
                  ^
        [3, 4, 5,  , 1] 2
                  ^
        [3, 4, 5,  , 1] 2
               ^
        [3, 4,  , 5, 1] 2
               ^
        [3, 4,  , 5, 1] 2
            ^
        [3,  , 4, 5, 1] 2
            ^
        [ , 3, 4, 5, 1] 2
            ^
        [ , 3, 4, 5, 1] 2
         ^
        [2, 3, 4, 5, 1]
    5. After the final step:
        > [2, 3, 4, 5,  ] 1
        > [2, 3, 4,  , 5] 1
        > [2, 3,  , 4, 5] 1
        > [2,  , 3, 4, 5] 1
        > [ , 2, 3, 4, 5] 1
        > [1, 2, 3, 4, 5]
    """

    for current_index, value in enumerate(array):
        inner_counter = current_index - 1
        while inner_counter >= 0:
            if array[inner_counter] > array[inner_counter+1]:
                array[inner_counter], array[inner_counter+1] = array[inner_counter+1], array[inner_counter]
            else:
                break
            inner_counter -= 1
    return array

if __name__ == "__main__":
    array = lambda: list("The quick brown fox jumps over the lazy dog".replace(" ","").lower())
    print sort(array())
