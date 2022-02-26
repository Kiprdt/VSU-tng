class Matrix:
    def __init__(self, line=0, column=0, elements=0):
        self.line = line
        self.column = column
        self.elements = elements
        self.spisok = []

    def input(self):
        self.line = int(input("Введите количество строк - "))
        self.column = int(input("Введите количество столбцов - "))
        if self.line > 3 or self.column > 3:
            print("Максимальная матрица - 3 x 3")
            exit()
        else:
            print("Заполните строки.")
        while len(self.spisok) != self.line:
            self.spisok.append([])
            while len(self.spisok[-1]) != self.column:
                self.elements = int(input("Ввод - "))
                self.spisok[-1].append(self.elements)
        else:
            return

    def __str__(self):
        return "\n".join(["\t".join(map(str, i)) for i in self.spisok])


a = Matrix()
a.input()
print(a)
