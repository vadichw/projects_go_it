# 'w'
file = open('lecture_1.txt', 'w',)
file.write('Hello, my Lord!\n')
file.write('Hi!\n')
file.writelines(['Odesa\n', 'Vadim\n','Vika\n'])
file.close()

# 'r' 
# можно не указывать, он идет по дефолту
file = open('lecture_1.txt', 'r',)
# Опасный метод
#result = file.read()

# Читает по одной строку
#result = file.readline()

# Читает все строки и записывает их в список 
result = file.readlines()
#print(result)
file.close()

# Добавить запись в существующий файл
# 'a'
# НЕ СТИРАЕТ ДАННЫЕ, а прост ДОБАВЛЯЕТ
file = open('lecture_1.txt', 'a')
file.write('The end\n')
file.close()


# Прочитати перші N рядки файлу
# Ім'я файлу для читання передамо як аргумент командного рядка

# import sys
# NUMBER_LINES = 4

#  1й - назва скрипта 2й - парамент, назва файлу
# if len(sys.argv) != 2:
#     #print("Error: Enter file name")
#     quit()
# try:
#     file = open(sys.argv[1], 'r')
#     line = file.readline()
#     count = 0
#     while count < NUMBER_LINES and line != "":
#         line = line.strip()
#         count += 1
#         print(line)
#         line = file.readline()
#     file.close()
# except OSError as err:
#     print(f"Error {err}")
    


# Прочитати хвіст файлу останні N рядки файлу
# Ім'я файлу для читання передамо як аргумент командного рядка

# import sys
# NUMBER_LINES = 4

# if len(sys.argv) != 2:
#     #print("Error: Enter file name")
#     quit()

# try:
#     lines = []
#     with open(sys.argv[1], 'r') as file:
#         for line in file:
#             lines.append(line)
#             if len(lines) > NUMBER_LINES:
#                 lines.pop(0)
#     print(lines)
# except OSError as err:
#     print(f"Error {err}")

# Читаем файл с помощью pathlib

# from pathlib import Path

# folder = Path('./Folder')
# filename = folder / 'new_text.txt'

# try:
#      with open(filename, 'r') as file:
#          for line in file:
#               print(line, end='') # end = '' шоб не было огромного отступа между абзацами
# except OSError as err:
#      print(f"Error!!! {err}")

# Можливості Pathlib

from pathlib import Path
# current_path = Path()
# print(current_path.cwd()) # .absolute

# #file = current_path / 'folder' / 'draw.svg'
# file = current_path.joinpath('draw', 'bin', '1', '2')
# print(file)
# print(file.parts)
# print(type(file.parts))
# print(file.name.split('.')[0])

# new_dir = Path('new_folder')
# new_dir.mkdir(exist_ok=True)
# new_dir.rmdir()

# # Parents folders
# new_dir = Path('test/new_folder')
# new_dir.mkdir(exist_ok=True, parents=True)
# new_dir.rmdir()

