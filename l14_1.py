def tmp(k):
    if k == []:
        return print('Конец списка.')
    print(k.pop(0))
    tmp(k)

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
tmp(my_list)