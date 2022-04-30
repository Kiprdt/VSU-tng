def mob(numbers, target):
    chart = {}
    for i in range(len(numbers)):
        discovery = target - numbers[i]
        if discovery in chart and chart[discovery] != i:
            return chart[discovery], i
        chart[numbers[i]] = i


assert mob([2, 4, 7, 9, 3], 7) == (1, 4)
assert mob([3, 2, 3], 6) == (0, 2)
assert mob([2, 3, 7, 4, 9], 7) == (1, 3)
assert mob([1, 5, 12, 2, 6], 13) == (0, 2)
assert mob([3, 2, 3], 6) == (0, 2)
assert mob([3, 3], 6) == (0, 1)
assert mob([3, 3, 2, 1, 3], 6) == (0, 1)
assert mob([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) == (0, 1)
assert mob([45, 92, 35, 21, 14, 2, 7], 9) == (5, 6)
