# todo: Преобразуйте переменную age и foo в число
# age = "23"
# foo = "23abc"
age = int("23")
foo = 23
print(type(age))
print(type(foo))
print()

# Преобразуйте переменную age в Boolean
age = "123abc"
age2 = bool(age)
print(type(age2))
print()

# Преобразуйте переменную flag в Boolean
flag = 1
flag2 = bool(flag)
print(type(flag2))
print()

# Преобразуйте значение в Boolean
str_one = "Privet"
str_two = ""
str_one2 = bool(str_one)
str_two2 = bool(str_two)
print(type(str_one2))
print(type(str_two2))
print()

# Преобразуйте значение 0 и 1 в Boolean
b = bool(0)
b2 = bool(1)
print(type(b))
print(type(b2))
print()

# Преобразуйте False в строку
bool = False
bool2 = str(bool)
print(type(bool2))
print()