from helpers import logger, caesar_cipher, caesar_decrypt

logger("Проверка работы логера")

text = "Hello, World!"
encrypted = caesar_cipher(text, 3)
decrypted = caesar_decrypt(encrypted, 3)

print("Исходный текст:", text)
print("Зашифрованный:", encrypted)
print("Расшифрованный:", decrypted)
