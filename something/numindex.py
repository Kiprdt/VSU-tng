def tgr(numbers, target):
    for i in range(len(numbers) - 1):
        a = target - numbers[i]
        if a in numbers:
            if i != numbers.index(a):
                return i, numbers.index(a)
            else:
                knowledge = i
                numbers[i] = 'None'
                for j in range(len(numbers) - 1):
                    return knowledge, numbers.index(a)


assert tgr([2, 3, 7, 4, 9], 7) == (1, 3)
assert tgr([1, 5, 12, 2, 6], 13) == (0, 2)
assert tgr([3, 2, 3], 6) == (0, 2)
assert tgr([3, 3], 6) == (0, 1)
assert tgr([3, 3, 2, 1, 3], 6) == (0, 1)
