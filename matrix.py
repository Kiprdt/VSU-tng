class Matrix:
    def __init__(self, line=1, column=1):
        self.line = line
        self.column = column
        self.spisok = [[0]]

    def input(self):
        self.line = int(input("Введите количество строк - "))
        self.column = int(input("Введите количество столбцов - "))
        for _ in range(self.line):
            self.spisok.append([])
            for _ in range(self.column):
                x = int(input("Ввод - "))
                self.spisok[-1].append(x)

    def __str__(self):
        return "\n".join(["\t".join(map(str, i)) for i in self.spisok])


a = Matrix()
a.input()
print(a)
