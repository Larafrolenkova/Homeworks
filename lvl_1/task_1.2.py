# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
print('Пункт A.')
sum = 0
i = len(my_favorite_songs)
for number in range(3):
    from random import randint
    x = randint(0, i-1)
    sum+=my_favorite_songs[x][1]
print('Три песни звучат', round(sum,2), 'минут')

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

print('Пункт B.')
sum = 0
key = list(my_favorite_songs_dict)
for number in range(3):
    from random import randint
    y = randint(0, len(key)-1)
    sum+=my_favorite_songs_dict.get(key[y])
print('Три песни звучат', round(sum,2), 'минут')

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random
print('Пункт С.')
sum_A = 0
sum_B = 0
i = len(my_favorite_songs)
key = list(my_favorite_songs_dict)
for number in range(3):
    from random import randint
    x = randint(0, i-1)
    y = randint(0, len(key)-1)
    sum_A+=my_favorite_songs[x][1]
    sum_B+=my_favorite_songs_dict.get(key[y])
print('Три песни из пункта А звучат', round(sum_A,2), 'минут')
print('Три песни из пункта B звучат', round(sum_B,2), 'минут')

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 
import datetime
print('Пункт D:')
for number in range(i):
    time_ = str(my_favorite_songs[number][1])
    time_ = time_.split('.')

    print(my_favorite_songs[number][0], datetime.time(0,int(time_[0]),int(time_[1])))
