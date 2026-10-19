import json
import logging
import requests
from bs4 import BeautifulSoup

URL = "https://quotes.toscrape.com"
HEADERS = {"User-Agent": "Mozilla/5.0"}

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)


def parse_quotes():
    logging.info("Загружаем страницу сайта...")

    response = requests.get(
        URL,
        headers=HEADERS,
        timeout=10
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")

    quotes = []

    for quote in soup.select("div.quote"):
        text_tag = quote.select_one("span.text")
        author_tag = quote.select_one("small.author")

        if text_tag and author_tag:
            quotes.append({
                "text": text_tag.get_text(strip=True),
                "author": author_tag.get_text(strip=True)
            })

    return quotes


if __name__ == "__main__":
    try:
        quotes = parse_quotes()

        with open("quotes.json", "w", encoding="utf-8") as file:
            json.dump(
                quotes,
                file,
                ensure_ascii=False,
                indent=2
            )

        logging.info("Спарсено цитат: %s", len(quotes))
        logging.info("Данные сохранены в quotes.json")

    except requests.RequestException as error:
        logging.error("Ошибка загрузки сайта: %s", error)
