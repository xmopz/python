# todo: База данных пользователя.
# Задан массив объектов пользователя
"""
Написать фильтр который будет выводить отсортированные объекты по возрасту(больше введеного)
,первой букве логина, и заданной группе.
#Сперва вводится тип сортировки:
1. По возрасту
2. По первой букве
3. По группе
тип сортировки: 1
#Затем сообщение для ввода
Ввидите критерии поиска: 16
Результат:
#Пользователь: 'Piter' возраст 23 года , группа  "admin"
#Пользователь: 'Dasha' возраст 30 лет , группа  "master"
"""

users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
         {'login': 'Ivan',  'age': 10, 'group': "guest"},
         {'login': 'Dasha', 'age': 30, 'group': "master"},
         {'login': 'Fedor', 'age': 13, 'group': "guest"}]

sort_type = int(input("Введите тип сортировки: "))
if 1 <= sort_type <= 3:
    match sort_type:
        case 1:
            search_age = int(input("Введите критерии поиска: "))
            for user in users:
                if user["age"] > search_age:
                    print(f"Пользователь {user['login']}, возраст {user['age']} лет, группа {user['group']}")
        case 2:
            first_letter = input("Введите критерии поиска: ").lower()
            for user in users:
                if user["login"].lower().startswith(first_letter):
                    print(f"Пользователь {user['login']}, возраст {user['age']} лет, группа {user['group']}")
        case 3:
            search_group = input("Введите критерии поиска: ").lower()
            for user in users:
                if user["group"].lower() == search_group:
                    print(f"Пользователь {user['login']}, возраст {user['age']} лет, группа {user['group']}")
else:
    print("Ошибка. Нужно ввести 1, 2 или 3")

