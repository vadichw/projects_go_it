# Сортування файлів у папці
# Копіювати файли з папки та покласти в іншу з тим же розширеням

import argparse
from pathlib import Path
from shutil import copyfile

parser = argparse.ArgumentParser(description='Sorting folder')
# ім'я змінної
parser.add_argument('--source', '-s', required=True, help='source folder') 
# результативна папка
parser.add_argument('--output', '-o', default='dist', help='output folder') 

args = vars(parser.parse_args()) # парсер vars поверне словник 
source = args.get('source')
output = args.get('output')

# print(f"{args}")
# print(source, output)

def read_folder(path: Path) -> None:
    for element in path.iterdir():
        if element.is_dir():
            read_folder(element)
        else:
            copy_file(element)


def copy_file(file: Path):
    ext = file.suffix
    new_path = output_folder / ext
    new_path.mkdir(exist_ok = True, parents = True)
    copyfile(file, new_path/file.name)


output_folder = Path(output)
read_folder(Path(source))



