#todo Задача 1. Чтение матрицы, load_matrix(filename)
""" Дан файл, содержащий таблицу целых чисел вида
(в каждой строке через пробел записаны числа)

11 12 13 14 15 16
21 22 23 24 25 26
31 32 33 34 35 36


Требуется написать функцию load_matrix(filename) которая загружает эту таблицу из файла.
Если в каждой строке находится одинаковое количество чисел, функция возвращает список списков целых чисел.
В противном случае возвращает False.

Задачу следует решить с использованием списковых включений, циклы использовать НЕЛЬЗЯ!"""

def load_matrix(filename):
    try:
        matrix = [
            [int(num) for num in line.split()]
            for line in open(filename, encoding="utf-8")
        ]

        return matrix if matrix and all(
            len(row) == len(matrix[0]) for row in matrix
        ) else False

    except (ValueError, OSError):
        return False
