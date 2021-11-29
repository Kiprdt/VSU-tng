def bin_search(sequence, x):
    sequence = sorted(sequence)
    left = 0
    right = len(sequence) - 1
    index = -1
    if x in sequence:
        while (left <= right) and (index == -1):
            mid = (left + right) // 2
            if sequence[mid] == x:
                index = mid
            else:
                if x < sequence[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return index
    return None


def bin_search_tests():
    assert bin_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 15, 17], 17) == 12
    assert bin_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 15, 17], 12) is None
    assert bin_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 1 ) == 0
    assert bin_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5 ) == 4
    assert bin_search([1, 3, 8, 4, 5, 7, 6, 2], 6) == 5
    assert bin_search([], 2) is None


z = [1, 2, 3, 4, 5, 6, 7]
x = 7
print(bin_search(z, x))
bin_search_tests()
