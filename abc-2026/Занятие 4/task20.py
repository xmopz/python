#todo: Выведите все строки данного файла в обратном порядке, допишите их в этот же файл.
# Для этого считайте список всех строк при помощи метода readlines().
"""
#Содержимое файла inverted_sort.txt
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.

# Результат
Complex is better than complicated.
Simple is better than complex.
Explicit is better than implicit.
Beautiful is better than ugly.
"""
file = open("inverted_sort.txt", "r+")

file_lines = file.readlines()
for i in range(len(file_lines)-1, -1, -1):
    print(file_lines[i])
    file.write(file_lines[i])
file.close()