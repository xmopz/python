import random
import pickle
import os

_dict = {
    "False": "Логическое значение — ложь",
    "None": "Отсутствующее или пустое значение",
    "True": "Логическое значение — истина",
    "and": "Логическое И",
    "as": "Задаёт другое имя для объекта",
    "assert": "Проверяет условие и сообщает об ошибке",
    "async": "Объявляет асинхронную функцию",
    "await": "Ожидает завершения асинхронной операции",
    "break": "Прерывает цикл",
    "class": "Создаёт класс",
    "continue": "Переходит к следующей итерации цикла",
    "def": "Создаёт функцию",
    "del": "Удаляет переменную или элемент",
    "elif": "Дополнительное условие",
    "else": "Выполняется, если условие не подошло",
    "except": "Обрабатывает ошибку",
    "finally": "Выполняется в конце обработки ошибки",
    "pass": "Ничего не делает",
    "for": "Цикл перебора элементов",
    "from": "Указывает источник импорта",
    "global": "Разрешает изменять глобальную переменную",
    "if": "Проверяет условие",
    "import": "Подключает модуль",
    "in": "Проверяет наличие элемента",
    "is": "Проверяет, являются ли объекты одним объектом",
    "lambda": "Создаёт короткую анонимную функцию",
    "nonlocal": "Разрешает изменять переменную внешней функции",
    "not": "Логическое НЕ",
    "or": "Логическое ИЛИ",
    "raise": "Вызывает ошибку вручную",
    "return": "Возвращает результат из функции",
    "try": "Запускает код, где возможна ошибка",
    "while": "Цикл, пока условие истинно",
    "with": "Безопасно работает с ресурсом",
    "yield": "Возвращает значение из генератора"
}

SAVE_FILE = "game_save.pkl"

def create_game():
    #сздаём новую игру/возвращаем её состояние
    secret = random.choice(list(_dict.keys()))

    return {
        "secret": secret,
        "mask": ["*"] * len(secret),
        "known_letter": set(),
        "hp": 3,
        "game_status": True
    }

def save_game(game):
    #cериализуем состояние игры/охраняем его в файл
    with open(SAVE_FILE, "wb") as file:
        pickle.dump(game, file)

    print("Игра сохранена")

def load_game():
    #загружаем состояние игры из файла
    if not os.path.exists(SAVE_FILE):
        print("Файл сохранения не найден")
        return None

    try:
        with open(SAVE_FILE, "rb") as file:
            game = pickle.load(file)

        print("Игра загружена")
        return game

    except (pickle.PickleError, EOFError, OSError):
        print("Не удалось загрузить сохранение")
        return None

def show_game(game):
    #вывод информации о текущей игре
    secret = game["secret"]

    print("\nОписание слова:", _dict[secret])
    print("Загаданное слово:", game["mask"])
    print("Количество букв:", len(secret))
    print("Количество попыток:", game["hp"])

def check_letter(game, letter):
    #проверка буквы /обновление состояние игры
    secret = game["secret"]
    letter = letter.lower()

    if len(letter) != 1 or not letter.isalpha():
        print("Введите одну букву!")
        return

    if letter in game["known_letter"]:
        print("Эта буква уже открыта!")
        return

    game["known_letter"].add(letter)

    found_letter = False

    for index, char in enumerate(secret):
        if char.lower() == letter:
            game["mask"][index] = char
            found_letter = True

    if found_letter:
        print("Вы угадали букву!")
        print(game["mask"])
    else:
        print("Вы не угадали букву!")
        game["hp"] -= 1
        print("Количество попыток:", game["hp"])

    if "*" not in game["mask"]:
        print("Победа! Вы угадали слово:", secret)
        game["game_status"] = False

    elif game["hp"] <= 0:
        print("Попытки закончились, вы проиграли!")
        print("Загаданным словом было:", secret)
        game["game_status"] = False


def play_game(game):
    #основной игровой цикл
    show_game(game)

    while game["game_status"]:
        print("\nВведите букву.")
        print("Команды: сохранить, выход")

        command = input("> ").strip()

        if command.lower() == "сохранить":
            save_game(game)
            continue

        if command.lower() == "выход":
            print("Выход из игры.")
            break

        check_letter(game, command)

def main():
    print("=== Поле чудес ===")
    print("1. Новая игра")
    print("2. Загрузить игру")

    choice = input("Выберите действие: ").strip()

    if choice == "2":
        game = load_game()

        if game is None:
            print("Начинаем новую игру.")
            game = create_game()
    else:
        game = create_game()

    play_game(game)

if __name__ == "__main__":
    main()
