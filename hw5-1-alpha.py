def bin_search(sequence, element):
    start = 0
    end = len(sequence)
    step = 0
    while start <= end:
        step += 1    # Количество шагов
        print("Subsequence in {}: {}".format(step, str(sequence[start:end + 1])))
        mid = (start + end) // 2    # Находим середину последовательности
        if element == sequence[mid]:
            return mid
        elif element < sequence[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return None


sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1001, 1002, 1004, 1005]
element = int(input("Введите искомый элемент."))
bin_search(sequence, element)
