#todo: Заданы множества
# все пользователи
# пользователи не в сети
# Вычислить пользователей online

all_users = {'id3', 'id5', 'id9', 'id8', 'id2', 'id1', 'id4', 'id6', 'id7', 'id10'}
offline_users = {'id3', 'id9', 'id7', 'id2', 'id4', 'id6'}
online_users = all_users.difference(offline_users)
print(online_users)