#todo: Взлом шифра
"""Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
Попробуйте все возможные сдвиги и расшифруйте фразу.


grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin.
"""
from helpers import caesar_decrypt

text = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."
for shift in range(26):
    print(f"Сдвиг {shift:2}: {caesar_decrypt(text, shift)}")
