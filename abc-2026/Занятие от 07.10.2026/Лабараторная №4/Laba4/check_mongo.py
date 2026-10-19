from db import get_collection

def check_database():
    collection = get_collection()

    try:
        # Проверяем подключение и наличие документов
        collection.database.client.admin.command("ping")

        count = collection.count_documents({})
        print("Подключение к MongoDB: успешно")
        print(f"База данных: {collection.database.name}")
        print(f"Коллекция: {collection.name}")
        print(f"Количество документов: {count}")

        print("\nПримеры сохранённых слов:")

        for document in collection.find({}, {"_id": 0}).limit(5):
            print(document)

        if count == 0:
            print("\nВ коллекции пока нет документов.")

    finally:
        collection.database.client.close()

if __name__ == "__main__":
    check_database()