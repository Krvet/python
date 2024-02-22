w = 'hello world'
f = 'ell'

index_w = 0
index_f = 0
len_w = len(w)
len_f = len(f)

while (index_w <= len_w - len_f) and (index_f < len_f):
    if w[index_w + index_f] == f[index_f]:
        index_f += 1
    else:
        index_w += 1
        index_f = 0

print(f"'{w}'")
print(f"'{f}'")

if index_f == len_f:
    print(f'Подстрока есть. Начало тут {index_w}')
else:
    print(f'Строки нет')
