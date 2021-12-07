def bin_search(sequence, x):
    left = 0
    right = len(sequence) - 1
    index = -1
    while (left <= right) and (index == -1):
        mid = (left + right) // 2
        if sequence[mid] == x:
            if sequence[mid - 1] == x:
                index = mid - 1
            else:
                index = mid
        else:
            if x < sequence[mid]:
                right = mid - 1
            else:
                left = mid + 1
    if right < left:
        return None
    return index


def bin_search_tests():
    assert bin_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 15, 17], 17) == 12
    assert bin_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 15, 17], 12) is None
    assert bin_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 1) == 0
    assert bin_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5) == 4
    assert bin_search([], 2) is None
    assert bin_search([1, 1, 2, 2, 3], 2) == 2
    assert bin_search([1, 1, 2, 2, 3, 4, 5, 6, 6, 7, 8], 6) == 7
    assert bin_search([1, 1, 2, 2, 3, 4, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8], 7) == 12
    assert bin_search([], 42) is None
    assert bin_search([0], 0) == 0
    assert bin_search([0], 1) is None
    assert bin_search([-1, 0, 42], 0) == 1
    assert bin_search([-42, 0, 42], 42) == 2
    assert bin_search([-6, -5, -4, -3, -2, -1], -4) == 2
    assert bin_search([1, 2, 3, 4, 5, 6], 4) == 3
    assert bin_search([1, 2, 3, 4, 5, 6, 7], 4) == 3
    assert bin_search([1, 2, 3, 4, 5], 7) is None
    assert bin_search([1, 2, 3, 4, 5, 6], 7) is None
    assert bin_search([42, 42, 42, 42, 42], 42) == 0
    assert bin_search([-42, -42, -42, -42, -42], -42) == 0
    assert bin_search([42, 42, 42, 42, 43], 43) == 4
    assert bin_search([41, 42, 42, 42, 42], 41) == 0
    assert bin_search([-2, -2, -1, 0, 1, 2, 2, 2], -1) == 2
    assert bin_search([-2, -2, -1, 0, 1, 1, 2, 2], 4) != 1


z = [1, 1, 2, 2, 3, 4, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8]
x = 7
print(bin_search(z, x))
bin_search_tests()
