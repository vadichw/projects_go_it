fh = open('text.txt', 'w')
sym_wr = fh.write('hello,world')
print(sym_wr)
# ЗАКРЫТЬВАТЬ ОБЯЗАТЕЛЬНО
fh.close()