class Matrix:
    def __init__(self, line=0, column=0, elements=0):
        self.line = line
        self.column = column
        self.elements = elements
        self.spisok = []

    def input(self):
        self.line = int(input("Введите количество строк"))
        self.column = int(input("Введите количество столбцов"))
        if self.line > 3 or self.column > 3:
            print("Не допустимые значения")
        else:
            while len(self.spisok) != self.column * self.line:
                self.elements = input("Введите эелементы")
                self.spisok.append(self.elements)
            else:
                return

    def __str__(self):
        return f"{self.spisok}" + "- элементы матрицы" + f"\n{self.line} - количество строк" +  f"\n{self.column} - количество столбцов"


a = Matrix()
a.input()
print(a)



spisok = [[1, 3, 4], [5, 6, 7], [1, 2, 3]]
for i in spisok:
    for k in i:
        print(k)
        
        
        class Matrix:
    def __init__(self, line=0, column=0, elements=0):
        self.line = line
        self.column = column
        self.elements = elements
        self.spisok = []
    def input(self):
        self.line = int(input("Введите количество строк"))
        self.column = int(input("Введите количество столбцов"))
        while len(self.spisok) != self.line:
            self.spisok.append([])
            while len(self.spisok[-1]) != self.column:
                self.elements = int(input("Ввод"))
                self.spisok[-1].append(self.elements)
            else:
                return 
        else:
            return

    def __str__(self):
        return f"{self.spisok}" + "- элементы матрицы"          


a = Matrix()
a.input()
print(a)
