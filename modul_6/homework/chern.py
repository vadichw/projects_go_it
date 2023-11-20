from pathlib import Path
import shutil
from normalize import normalize
import sys

def handle_media(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok = True, parents = True)
    filename.replace(target_folder / normalize(filename.name)) # важно name ибо нормалайз принимает нейм

def handle_archive(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok = True, parents = True)
    forler_for_file= target_folder / normalize(filename.name.replace(filename.suffix, ""))
    forler_for_file.mkdir(exist_ok = True, parents = True)

    try:
        shutil.unpack_archive(filename.resolve(), forler_for_file.resolve())

    except shutil.ReadError:
        print("It s not archive")
        forler_for_file.rmdir()

        return None

path = sys.argv[1]

