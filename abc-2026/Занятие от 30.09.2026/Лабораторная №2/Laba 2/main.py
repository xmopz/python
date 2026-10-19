
import random

from db import get_collection


def create_game(collection):
    words = list(collection.find({}))

    if not words:
        print("В базе нет слов, запустите seed.py")
        return None

    word_data = random.choice(words)
    secret = word_data["word"]

    return {
        "word_id": word_data["_id"],
        "secret": secret,
        "hint": word_data["hint"],
        "category": word_data["category"],
        "mask": ["*"] * len(secret),
        "known_letter": set(),
        "hp": 3,
        "game_status": True,
    }


def show_game(game):
    print("\nКатегория:", game["category"])
    print("Описание слова:", game["hint"])
    print("Загаданное слово:", game["mask"])
    print("Количество букв:", len(game["secret"]))
    print("Количество попыток:", game["hp"])


def check_letter(game, letter, collection):
    secret = game["secret"]
    letter = letter.lower()

    if len(letter) != 1 or not letter.isalpha():
        print("Введите одну букву")
        return

    if letter in game["known_letter"]:
        print("Эта буква уже открыта")
        return

    game["known_letter"].add(letter)
    found_letter = False

    for index, char in enumerate(secret):
        if char.lower() == letter:
            game["mask"][index] = char
            found_letter = True

    if found_letter:
        print("Вы угадали букву")
        print(game["mask"])
    else:
        print("Вы не угадали букву")
        game["hp"] -= 1
        print("Количество попыток:", game["hp"])

    if "*" not in game["mask"]:
        print("Победа! Вы угадали слово:", secret)

        collection.update_one(
            {"_id": game["word_id"]},
            {"$inc": {"guessed_count": 1},
             "$set": {"used": True}},
        )

        game["game_status"] = False

    elif game["hp"] <= 0:
        print("Попытки закончились, вы проиграли")
        print("Загаданным словом было:", secret)

        collection.update_one(
            {"_id": game["word_id"]},
            {"$set": {"used": True}},
        )

        game["game_status"] = False


def play_game(collection):
    game = create_game(collection)

    if game is None:
        return

    show_game(game)

    while game["game_status"]:
        print("\nВведите букву.")
        print("Команды: выход")

        command = input("> ").strip()

        if command.lower() == "выход":
            print("Выход из игры.")
            break

        check_letter(game, command, collection)


def main():
    print("=== Поле чудес ===")

    collection = get_collection()

    try:
        # Проверяем соединение с MongoDB
        collection.database.client.admin.command("ping")
        print("Подключение к MongoDB успешно")

        while True:
            print("\n1. Новая игра")
            print("2. Выход")

            choice = input("Выберите действие: ").strip()

            if choice == "1":
                play_game(collection)
            elif choice == "2":
                print("бай")
                break
            else:
                print("Неверный выбор")

    except Exception as error:
        print("Ошибка подключения или работы с MongoDB:", error)

    finally:
        collection.database.client.close()


if __name__ == "__main__":
    main()
