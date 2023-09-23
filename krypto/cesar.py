def cesar(alfabet: str, shift: int, word: str, state: int) -> str:
    final_word = ''
    for i in word.upper():
        place = alfabet.find(i)
        if state == 1:
            new_place = (place + shift) % len(alfabet)
        else:
            new_place = (place - shift) % len(alfabet)
        if i in alfabet:
            final_word += alfabet[new_place]
        else:
            final_word += i
    return final_word


#alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
#alfavit_EU =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

