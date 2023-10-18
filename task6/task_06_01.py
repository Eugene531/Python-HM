import random


class Matrix:
    """
        Класс для реализации дейсвтия с матрицами.

        Args:
            *args: Переменное число аргументов.
                Если передан один аргумент, считается, что это двумерный список матрицы.
                Если переданы два аргумента: 1- количество строк, 2 - количество столбцов.

        Attributes:
            matrix (list): Список, представляющий матрицу.
    """
    def __init__(self, *args) -> None:
        self.matrix = []
        if len(args) == 1:
            self.matrix = list(args)
        else:
            for _ in range(args[0]):
                self.matrix += [list(random.choices(range(20), k=args[1]))]


    def __str__(self):
            """
            Возвращает строковое представление матрицы.

            Returns:
                str: Строковое представление матрицы, разделенное табуляциями.
            """
            return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])


    def __add__(self, other):
        """
        Сложение матриц.

        Args:
            other (Matrix): Другая матрица, с которой производится сложение.

        Returns:
            Matrix: Результат сложения матриц.

        Raises:
            ValueError: Если размеры матриц не совпадают.
        """
        if (len(self.matrix) != len(other.matrix) 
            or len(self.matrix[0]) != len(other.matrix[0])):
            raise ValueError
        result = [
                    [
                    self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))
                    ]
                for i in range(len(self.matrix))
                ]
        return Matrix(result)


    def __sub__(self, other):
        """
        Вычитание матриц.

        Args:
            other (Matrix): Другая матрица, из которой производится вычитание.

        Returns:
            Matrix: Результат вычитания матриц.

        Raises:
            ValueError: Если размеры матриц не совпадают.
        """
        if (len(self.matrix) != len(other.matrix) 
            or len(self.matrix[0]) != len(other.matrix[0])):
            raise ValueError
        result = [
                    [
                    self.matrix[i][j] - other.matrix[i][j] for j in range(len(self.matrix[0]))
                    ] 
                for i in range(len(self.matrix))
                ]
        return Matrix(result)


    def __mul__(self, other):
        """
        Умножение матрицы на скаляр или на другую матрицу.

        Args:
            other: Если является целым числом, матрица умножается на скаляр.
                   Если другой экземпляр Matrix, матрица умножается на эту матрицу.

        Returns:
            Matrix: Результат умножения.

        Raises:
            ValueError: Если количество столбцов в первой матрице не совпадает со второй.
        """
        if isinstance(other, int):
            result = [
                        [
                            self.matrix[i][j] * other for j in range(len(self.matrix[0]))
                        ]
                    for i in range(len(self.matrix))
                    ]
            return Matrix(result)
        elif len(self.matrix[0]) != len(other.matrix):
            raise ValueError
        result = [
                    [
                        sum(
                            self.matrix[i][k] * other.matrix[k][j] for k in range(len(self.matrix[0]))
                            ) for j in range(len(other.matrix[0]))
                    ]
                for i in range(len(self.matrix))
                ]
        return Matrix(result)
    

    def __rmul__(self, other):
        """
        Умножение справа.
        """
        return self * other
    

    def transpose(self):
        """
        Транспонирование матрицы.

        Returns:
            Matrix: Транспонированная матрица.
        """
        result = [
                [
                    self.matrix[j][i] for j in range(len(self.matrix))
                ] for i in range(len(self.matrix[0]))
            ]
        return Matrix(result)


    def is_square(self):
        """
        Проверяет, является ли матрица квадратной.

        Returns:
            bool: True, если матрица квадратная, иначе False.
        """
        return len(self.matrix) == len(self.matrix[0])


    def is_symmetric(self):
        """
        Проверяет, является ли квадратная матрица симметричной относительно
        главной (побочной) диагонали.

        Returns:
            bool: True, если матрица симметрична, иначе False.
        """
        if not self.is_square():
            return False
        return all(
                self.matrix[i][j] == self.matrix[j][i] for i in range(len(self.matrix)) 
                for j in range(i+1, len(self.matrix[0]))
                )


    def __eq__(self, other):
        """
        Проверяет, равны ли две матрицы.

        Args:
            other (Matrix): Другая матрица для сравнения.

        Returns:
            bool: True, если матрицы равны, иначе False.
        """
        return self.matrix == other.matrix
