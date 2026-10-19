import json
import logging
from db import get_collection

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

def import_words():
    with open("game_words.json", "r", encoding="utf-8") as file:
        words = json.load(file)

    collection = get_collection()

    try:
        for item in words:
            collection.update_one(
                {"word": item["word"]},
                {"$setOnInsert": item},
                upsert=True
            )

        logging.info("Обработано слов: %s", len(words))
        logging.info(
            "Всего документов в коллекции: %s",
            collection.count_documents({})
        )
    finally:
        collection.database.client.close()

if __name__ == "__main__":
    import_words()