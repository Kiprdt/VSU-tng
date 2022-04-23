def tgr(numbers, target):
    for i in range(len(numbers) - 1):
        a = target - numbers[i]
        if a in numbers:
            return i, numbers.index(a)


assert tgr([2, 3, 7, 4, 9], 7) == (1, 3)
assert tgr([1, 5, 12, 2, 6], 13) == (0, 2)
