# Реалізуйте функцію create_backup(path, file_name, employee_residence)

# Де:
# path — шлях до файлу
# file_name — ім'я файлу
# employee_residence — словник, у якому ключ — ім'я користувача, а значення — країна проживання. Вигляд: {'Michael': 'Canada', 'John':'USA', 'Liza': 'Australia'}

# Функція повинна працювати так:
# Створювати бінарний файл file_name за шляхом path
# Зберігати дані словника employee_residence у файл, де кожен новий рядок — це ключ значення через пробіл як "Michael Canada"
# Архівувати теку по шляху path за допомогою shutil
# Ім'я архіву має бути backup_folder.zip
# Функція має повернути рядок шляху до архіву backup_folder.zip

# Вимоги:
# запишіть вміст словника employee_residence у бінарний файл з ім'ям file_name у теку path за допомогою оператора with.
# використовуйте символ /, щоб розділити шлях для path та file_name
# вигляд рядка файлу — Michael Canada, в кінці кожного рядка додається перенесення рядка '\n'.
# при збереженні кожен рядок файлу кодується методом encode
# при записі рядків використовуємо лише метод write
# архів має бути у форматі zip з ім'ям 'backup_folder', створений за допомогою make_archive.




import shutil

def create_backup(path, file_name, employee_residence):
    # Запис словника у бінарний файл
    with open(f"{path}/{file_name}", 'wb') as file:
        for name, country in employee_residence.items():
            # Записуємо дані у файл у форматі "Ім'я Країна\n"
            line = f"{name} {country}\n"
            file.write(line.encode())

    # Архівація теки
    backup_folder_name = 'backup_folder'
    shutil.make_archive(f"{backup_folder_name}", 'zip', path)

    # Повертаємо шлях до створеного архіву
    return f"{path}/{backup_folder_name}.zip"