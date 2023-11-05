from pathlib import Path

p = Path('E:/repos/projects_go_it/modul_4')
print(p)

for elements in p.iterdir():
    print(elements.name)

# Можна викликати Path без аргументів, тоді ви отримаєте вказівник на папку, в якій ви зараз знаходитеся.
