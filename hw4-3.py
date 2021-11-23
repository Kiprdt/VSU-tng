def check_sequence(k):
    return len(set(k)) == len(k)


def check_sequence_tests():
    assert check_sequence([1, 1, 2, 2, 3, 4, 5, 6]) == False
    assert check_sequence([21, 44, 56, 32, 19, 40]) == True
    assert check_sequence([58, 1009, 2, 1009, 107, 908]) == False
    assert check_sequence([9, 8, 32, 89, 1, 56]) == True


z = [1, 22, 22, 3, 4, 8, 8, 10]
print(check_sequence(z))
check_sequence_tests()
