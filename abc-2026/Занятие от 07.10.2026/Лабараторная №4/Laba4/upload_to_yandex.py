import os
import sys
import logging
import requests
from pathlib import Path

TOKEN = os.getenv("YANDEX_DISK_TOKEN")
API_URL = "https://cloud-api.yandex.net/v1/disk/resources"

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

def upload_file(local_file, disk_path):
    if not TOKEN:
        raise ValueError("Не задан YANDEX_DISK_TOKEN")

    file_path = Path(local_file)

    if not file_path.is_file():
        raise FileNotFoundError(f"Файл не найден: {local_file}")

    headers = {"Authorization": f"OAuth {TOKEN}"}

    # Получаем ссылку для загрузки
    params = {
        "path": disk_path,
        "overwrite": "true"
    }

    response = requests.get(
        f"{API_URL}/upload",
        headers=headers,
        params=params,
        timeout=30
    )
    response.raise_for_status()

    upload_url = response.json()["href"]

    # Загружаем содержимое файла
    with file_path.open("rb") as file:
        upload_response = requests.put(
            upload_url,
            data=file,
            timeout=120
        )

    upload_response.raise_for_status()
    logging.info("Файл загружен: %s", disk_path)

    # Проверяем наличие файла на Диске
    check_response = requests.get(
        API_URL,
        headers=headers,
        params={"path": disk_path},
        timeout=30
    )
    check_response.raise_for_status()

    metadata = check_response.json()
    logging.info(
        "Проверка успешна: %s, размер: %s байт",
        metadata.get("name"),
        metadata.get("size")
    )


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(
            'Использование: python upload_to_yandex.py '
            '"путь_к_локальному_файлу" "путь_на_Диске"'
        )
        sys.exit(1)

    try:
        upload_file(sys.argv[1], sys.argv[2])
    except requests.HTTPError as error:
        response = error.response
        logging.error(
            "Ошибка API: статус %s, ответ: %s",
            response.status_code,
            response.text
        )
        sys.exit(1)

    except requests.RequestException as error:
        logging.error("Ошибка соединения: %s", error)
        sys.exit(1)

    except FileNotFoundError as error:
        logging.error("%s", error)
        sys.exit(1)