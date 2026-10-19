import json
import logging
import requests
from bs4 import BeautifulSoup

URL = "https://docs.python.org/3/glossary.html"

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)


def parse_words():
    response = requests.get(
        URL,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=15
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")
    words = []

    for term in soup.select("dt"):
        definition = term.find_next_sibling("dd")

        if definition is None:
            continue

        # Убираем ссылку на заголовок, если она есть
        for link in term.select("a.headerlink"):
            link.decompose()

        name = term.get_text(" ", strip=True)
        hint = definition.get_text(" ", strip=True)

        # Для игры подходят короткие названия из букв
        if (
            name
            and hint
            and name.isascii()
            and name.replace("_", "").isalnum()
            and 2 <= len(name) <= 20
        ):
            words.append({
                "word": name.upper(),
                "category": "Python",
                "hint": hint,
                "source": URL,
                "used": False,
                "guessed_count": 0
            })

    # Убираем дубликаты
    unique = {item["word"]: item for item in words}
    return list(unique.values())


if __name__ == "__main__":
    words = parse_words()

    with open("game_words.json", "w", encoding="utf-8") as file:
        json.dump(words, file, ensure_ascii=False, indent=2)

    logging.info("Найдено слов: %s", len(words))
    logging.info("Результат сохранён в game_words.json")