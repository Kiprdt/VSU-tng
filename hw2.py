#(a * b - c) / (f - d)
print("Программа высчитывает выражение: (a * b - c) / (f - d)")
print("Пожалуйста, введите значения для каждой переменной")
print("Введите значение для 'a' ")
a = int(input())
print("Введите значение для 'b' ")
b = int(input())
print("Введите значение для 'c' ")
c = int(input())
print("Введите значение для 'f' ")
f = int(input())
print("Введите значение для 'd' ")
d = int(input())
if f - d == 0:
    print("Делить на нуль нельзя, проверьте переменные 'f' и 'd' ")
s = (a * b - c) / (f - d)
print("Ответ:", s)