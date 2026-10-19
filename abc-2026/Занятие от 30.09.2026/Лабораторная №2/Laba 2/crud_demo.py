from pymongo import MongoClient
from bson.objectid import ObjectId

# Подключение
client = MongoClient("mongodb://admin:admin123@localhost:27017/")
db = client["pole_chudes_db"]
collection = db["words"]

# ---------- CREATE ----------
# Вставка одного документа
word1 = {
 "word": "КОСМОНАВТ",
 "category": "Профессии",
 "hint": "Человек, работающий в космосе",
 "difficulty": "средняя",
 "used": False,
 "guessed_count": 0
}
result = collection.insert_one(word1)
print("Inserted id:", result.inserted_id)

# Вставка нескольких документов
words = [
 {"word": "ПИРАМИДА", "category": "Архитектура", "hint":
"Древнее сооружение в Египте",
 "difficulty": "лёгкая", "used": False, "guessed_count": 0},
 {"word": "ГИТАРА", "category": "Музыка", "hint": "Струнный инструмент",
 "difficulty": "лёгкая", "used": False, "guessed_count": 0},
 {"word": "АЛГОРИТМ", "category": "IT", "hint":
"Последовательность действий",
 "difficulty": "сложная", "used": False, "guessed_count": 0},
]
result = collection.insert_many(words)
print("Inserted ids:", result.inserted_ids)

# ---------- READ ----------
# Найти один документ
word = collection.find_one({"category": "Музыка"})
print("Найдено:", word)

# Найти все документы
for w in collection.find({"difficulty": "лёгкая"}):
 print(w["word"], "-", w["hint"])

# С проекцией (только нужные поля)
for w in collection.find({}, {"_id": 0, "word": 1, "category":
1}):
 print(w)

# ---------- UPDATE ----------
# Обновить одно поле
collection.update_one(
 {"word": "ГИТАРА"},
 {"$set": {"difficulty": "средняя"}}
)
# Инкремент счётчика
collection.update_one(
 {"word": "КОСМОНАВТ"},
 {"$inc": {"guessed_count": 1}}
)
# Массовое обновление
collection.update_many(
 {"used": False},
 {"$set": {"used": True}}
)

# ---------- DELETE ----------
# Удалить один документ
collection.delete_one({"word": "АЛГОРИТМ"})
# Удалить по условию
collection.delete_many({"difficulty": "сложная"})