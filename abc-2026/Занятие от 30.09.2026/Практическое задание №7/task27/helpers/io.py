from datetime import datetime


def logger(message, filename="log.txt"):
    """Записывает сообщение с датой и временем в файл."""
    with open(filename, "a", encoding="utf-8") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] {message}\n")
