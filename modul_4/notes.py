#------------------ THE LISTS----------------#

# CLEAR()
num = [1,2,3]
print(num)
num.clear()
print(num)

# EXTEND
num = [1,2,3]
char = ["a", "b", "c"]
num.extend(char)
print(num)

# FIND INDEX()
chars = ['a', 'b', 'c', 'd']
c_ind = chars.index('d')
print(c_ind)

#COUNT()
chars = ['a', 'b', 'c', 'a']
ch_a = chars.count('a')
print(ch_a)

#COPY()
chars =  ['a', 'b']
cop = chars.copy()
print(cop)


#----------------Dictionary--------------------#

# pop(key) — повертає значення елементу і видаляє пару ключ-значення зі словника

chars = {'a': 1, 
         'b': 2,}
b_ch = chars.pop('b')
print(b_ch)
print(chars)

# update(another_dict) — розширює словник значеннями з іншого словника
chars = {'a': 1, 'b': 2}
chars.update({"c": 3})
print(chars)

# get(key[, default]) — не викликає виключення, якщо ключа немає в словнику, повертає default, за замовчуванням default=None
chars = {'a': 1, 'b': 2}
c_idx = chars.get('c', -1)
print(c_idx)

# keys(), value()

num = {
    1: "one",
    2: "two",
    3: "three",
}

for n in num.keys():
    print(n)

for nv in num.values():
    print(nv)

for key, value in num.items():
    print(key, value)
