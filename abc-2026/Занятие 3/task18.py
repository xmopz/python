#todo: Заданы множества
#Даны читатели книг
#Даны читатели газет
# Найти пользователей кто читает и книги и газеты

readers_books = {'id3', 'id5', 'id9', 'id8', 'id2', 'id1' }
readers_magazines = { 'id8', 'id2', 'id1', 'id4', 'id6', 'id7', 'id10'}
readers_all = readers_books.intersection(readers_magazines)
print(readers_all)