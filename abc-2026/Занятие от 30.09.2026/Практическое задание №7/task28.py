#todo: Числа в буквы
"""Замените числа, написанные через пробел, на буквы. Не числа не изменять.

Пример.
Input	                            Output
8 5 12 12 15	                    hello
8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!
"""

def numbers_to_letters(text):
    result = []

    for token in text.split():
        if token.isdigit() and 0 <= int(token) <= 25:
            result.append(chr(ord("a") + int(token)))
        else:
            result.append(token)

    return " ".join(result)

text = input("Введите числа и текст: ")
print(numbers_to_letters(text))
