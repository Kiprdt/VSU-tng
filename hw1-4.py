a = input("Введите число или слово! :) >>")
if a == a[::-1]:
    print(a, "- Это палиндром!")
else:
    print(a, "- Это совсем не палиндром!")
