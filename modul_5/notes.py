#\n Перенесення рядка
#\f	Перенесення сторінки
#\r	Повернення каретки
#\t	Горизонтальна табуляція
#\v	Вертикальна табуляція

jingle_bells = "Jingle bells, jingle bells\nJingle all the way\nOh, what fun it is to ride\nIn a one horse open sleigh"

print(jingle_bells)

###-------------------------String Methogs-------------###

# find()
# Повертає -1, якщо послідовність не знайдена.
# Цей метод виводить індекс початку першого збігу в рядку s, починаючи з start до end. Якщо start та end не вказані, то з початку і до кінця 
# Поиск идет СЛЕВА

s = "Hi there!"

#start = 0
#end = 7

print(s.find("er")) 
print(s.find("A"))
#index()
print(s.index("h"))

#Можно искать СПРАВА
word = 'some word'
print(word.rfind('d'))
print(word.rindex("d"))

### SPLIT ###
#Для такого завдання можна скористатися методом split, який приймає як аргумент підрядок-маркер, який буде межею, по якій потрібно розбити рядок на частини. В результаті виклику повертається список рядків.

s = "I am learning strings in Python. Some new methods got now."
sentence = s.split('. ')
print(sentence[0])
print(sentence[1])

# Удалает пробелы (strip, rstrip, lstrip)
clean = '   spacious   '.strip()
print(clean)

# replace()
dogs_text = "All dogs bark like dogs."
cats_text = dogs_text.replace("dogs", "cats")
print(dogs_text)
print(cats_text)

# Для видалення фіксованої послідовності НА ПОЧАТКУ рядка є метод removeprefix
print('TestHook'.removeprefix('Test'))
print('TestHook'.removeprefix('Hook')) # Не удалил, ибо ХУК в конце

# Є парний метод для видалення послідовності в кінці рядка, removesuffix
print('TestHook'.removesuffix('Hook'))
print('TestHook'.removesuffix('Test'))