#todo: Дан массив размера N. Найти минимальное растояние между одинаковыми значениями в массиве и вывести их индексы.
# Одинаковых значение может быть два и более !
# Пример:
# mass = [1,2,17,54,30,89,2,1,6,2]
# Для числа 1 минимальное растояние в массиве по индексам: 0 и 7
# Для числа 2 минимальное растояние в массиве по индексам: 6 и 9
# Для числа 17 нет минимального растояния т.к элемент в массиве один.

array_size = int(input("Введите длинну массива: "))
array = [0] * array_size

for i in range(array_size):
    array[i] = int(input("Введите числа для массива: "))
print(array)

for index, number in enumerate(array): #Вроде ничего сложного нет в задании
    if number in array[:index]:             #Но далось оно почему то тяжело
        continue                            #Уверен это не самое лучшее и компактное решение
    min_distance = 10000000                 #Но что бы реализовать хотя бы его
    index_1 = -1                            #Пришлось сидеть и гуглить :(
    index_2 = -1
    found = False
    for index2 in range(index + 1, len(array)):
        number2 = array[index2]
        if number == number2 and index != index2:
            distance = abs(index2 - index)
            if distance < min_distance:
                min_distance = distance
                index_1 = index
                index_2 = index2
                found = True
    if found:
        print(f"Для числа {number} минимальное расстояние в массиве по индексам: {index_1} и {index_2}")
    else:
        print(f"Для числа {number} нет минимального расстояния тк элемент в массиве один")

