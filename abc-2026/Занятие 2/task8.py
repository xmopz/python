# todo: Проверить истинность высказывания:
# "Данное четырехзначное число читается одинаково слева направо и справа налево".

x = input("Введите четырёхзначное число: ")

def is_palindrome(num):
    if num == num[::-1]:
        return True
    else:
        return False

print(is_palindrome(x))
