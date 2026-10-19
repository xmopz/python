import logging
from typing import Optional
from pymongo import MongoClient
from pymongo.errors import PyMongoError
from .config import Config

logger = logging.getLogger(__name__)
class MongoDB:
    def __init__(self, config: Config):
        self.config = config
        self._client: Optional[MongoClient] = None
        self._db = None

    def connect(self) -> bool:
        try:
            if self._client is None:
                self._client = MongoClient(
                    self.config.mongo_uri,
                    serverSelectionTimeoutMS=self.config.MONGO_TIMEOUT_MS,
                    retryWrites=True,
                    retryReads=True,
                )
            self._client.admin.command("ping")
            self._db = self._client[self.config.MONGO_DB]

            logger.info("Подключение к MongoDB установлено")
            return True

        except PyMongoError as e:
            logger.error("Ошибка подключения к MongoDB: %s", e)

            if self._client is not None:
                self._client.close()

            self._client = None
            self._db = None
            return False

    def close(self):
        if self._client is not None:
            self._client.close()
            self._client = None
            self._db = None
            logger.info("Соединение с MongoDB закрыто")

    @property
    def db(self):
        if self._db is None:
            if not self.connect():
                raise RuntimeError("Не удалось подключиться к MongoDB")
        return self._db

    def ping(self) -> bool:
        if self._client is None:
            return self.connect()

        try:
            self._client.admin.command("ping")
            return True
        except PyMongoError as e:
            logger.error("Проверка MongoDB не пройдена: %s", e)
            return False
# Глобальный экземпляр
mongo = MongoDB(Config())
