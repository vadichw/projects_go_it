# Створіть функціонал для розпакування архіву.
# Зробіть import пакету shutil
# Створіть функцію unpack(archive_path, path_to_unpack), яка викликатиме метод пакета shutil unpack_archive та розпаковуватиме архів archive_path у місце path_to_unpack.
# Функція нічого не повертає.

import shutil

def unpack(archive_path, path_to_unpack):
    archived = shutil.unpack_archive(archive_path, path_to_unpack )
