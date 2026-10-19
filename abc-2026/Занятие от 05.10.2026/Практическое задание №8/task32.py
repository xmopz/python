# Инкапсуляция и property
# todo: Класс "Пользователь" (Валидация email)
# Создайте класс User. У него должны быть свойства email и password.
# При установке email проверяйте, что строка содержит символ @ (простая валидация).
# При установке пароля, храните не сам пароль, а его хеш (для простоты можно использовать hash()).
# Сделайте метод check_password(password), который проверяет, соответствует ли хеш переданного
# пароля сохраненному хешу.
"""
# Пример использования
user = User("test@example.com", "secret")
print(user.email)  # test@example.com
# print(user.password) # AttributeError
print(user.check_password("secret"))  # True
print(user.check_password("wrong"))   # False
"""

class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Email должен содержать символ @")
        self._email = value

    @property
    def password(self):
        raise AttributeError("Пароль нельзя прочитать напрямую")

    @password.setter
    def password(self, value):
        self._password_hash = hash(value)

    def check_password(self, password):
        return self._password_hash == hash(password)

user = User("test@example.com", "secret")
print(user.email)
print(user.check_password("secret"))
print(user.check_password("wrong"))
