# Наступне завдання буде суто теоретичним, і ми потренуємося працювати з довільною кількістю аргументів.
#Створіть дві функції:
# перша first буде мати першим параметром змінну size, а також вона може приймати будь-яку кількість позиційних аргументів. Функція повинна повернути суму size із загальною кількістю переданих до неї позиційних аргументів.
# друга функція second так само матиме першим параметром size і прийматиме довільну кількість ключових аргументів, і також має повернути суму size з кількістю переданих у функцію ключових аргументів.

def first(size, *top):
    sum = size + len(top)
    return sum

def second(size, **tops):
    sum = size + len(tops)
    return sum