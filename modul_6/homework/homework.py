import sys
import shutil, re
from pathlib import Path
from normalize import normalize



def create_folder(item):
    if item.is_file():
        file_name, file_ext = item.stem, item.suffix 
        file_ext = file_ext.lower()

        images = ('.jpeg', '.png', '.jpg', '.svg')
        documents = ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx')
        audio = ('.mp3', '.ogg', '.wav', '.amr')
        video = ('.avi', '.mp4', '.mov', '.mkv')
        archives = ('.zip', '.gz', '.tar')

        file_name = normalize(file_name)
        normalize_name = file_name + file_ext
        
        if file_ext in images:
            Path.mkdir(item.parent / 'images', exist_ok=True)
            item.rename(item.parent / 'images' / normalize_name)
        elif file_ext in documents:
            Path.mkdir(item.parent / 'documents', exist_ok=True)
            item.rename(item.parent / 'documents' / normalize_name) 
        elif file_ext in audio:
            Path.mkdir(item.parent / 'audio', exist_ok=True)
            item.rename(item.parent / 'audio' / normalize_name)    
        elif file_ext in video:
            Path.mkdir(item.parent / 'video', exist_ok=True)
            item.rename(item.parent / 'video' / normalize_name)  
            
        elif file_ext in archives:
            try:
                Path.mkdir(item.parent / 'archives', exist_ok=True)
                item.rename(item.parent / 'archives' / normalize_name)
                shutil.unpack_archive(Path(item.parent / 'archives' / normalize_name), Path(item.parent / 'archives' / file_name))
            except shutil.ReadError:
                print("File can't be procceeded, please check if it's archive.")
            
  
def sorter(path):
    ignore_list = ('archives', 'video', 'audio', 'documents', 'images')
    for item in path.glob('*'):
        if item.is_dir() and item.name not in ignore_list:
            sorter(item)
            if not list(item.glob('*')):
                item.rmdir()
        elif item.is_file():
            print(f'file {item}')
            print(item.parent)
            create_folder(item)
            
            
path = Path(sys.argv[1])
sorter(path)