#todo: Написать программу, которая считывает два числа и выводит их сумму, разность, частное, произведение,
# результат целочисленного деления, результат деления с остатком, результат возведения в степень.

x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))

def sum(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return "Нельзя делить на 0"
    else:
        return x / y

def div_int(x, y):
    if y == 0:
        return "Нельзя делить на 0"
    else:
        return x // y

def div_with_remainder(x, y):
    if y == 0:
        return "Нельзя делить на 0"
    else:
        return x % y

def raising(x, y):
    return x ** y

print("Сумма =", sum(x, y))
print("Разность =", sub(x, y))
print("Произведение =", mult(x, y))
print("Частное =", div(x, y))
print("Целочисленное деление =", div_int(x, y))
print("Остаток от деления =", div_with_remainder(x, y))
print("Возведение в степень =", raising(x, y))