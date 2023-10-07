def luna(string: [str, int]):
    ch = ''
    for i, k in enumerate(str(string)):
        if i % 2 == 0 or i == 0:
            define = int(k) * 2
            if define >= 10:
                ch += str(define // 10 + define % 10)
            else:
                ch += str(define)
        else:
            ch += k
    sum_of_numbers = sum(int(x) for x in ch)
    return 10 - (sum_of_numbers % 10)
