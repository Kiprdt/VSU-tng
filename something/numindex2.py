def tgr(numbers, target):
    for i in range(len(numbers)):
        a = target - numbers[i]
        if a in numbers and i != numbers.index(a):
            return i, numbers.index(a)
        elif a not in numbers:
            continue
        else:
            knowledge = i
            numbers[i] = 'None'
            return knowledge, numbers.index(a)


assert tgr([2, 3, 7, 4, 9], 7) == (1, 3)
assert tgr([1, 5, 12, 2, 6], 13) == (0, 2)
assert tgr([3, 2, 3], 6) == (0, 2)
assert tgr([3, 3], 6) == (0, 1)
assert tgr([3, 3, 2, 1, 3], 6) == (0, 1)
assert tgr([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) == (0, 1)
assert tgr([45, 92, 35, 21, 14, 2, 7], 9) == (5, 6)
