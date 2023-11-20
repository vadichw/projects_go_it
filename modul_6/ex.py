import argparse
from pathlib import Path
from shutil import copyfile

parser = argparse.ArgumentParser(description='Sorting folder')
parser.add_argument('--source', '-s', required= True, help='sourse folder')
parser.add_argument('--output', '-o', default='created folder', help='output folder')
argv = vars(parser.parse_args())
source = argv.get('source')
output = argv.get('output')


print(argv)
print(source)
print(output)