import random

def pl(t):
    for i in t:
        print(i)

s = int(input(f"Задайте количество матриц: "))
n = int(input(f"Задайте количество столбцов в матрице: "))
k = int(input(f"Задайте длину столбцов в матрице: "))

tmp1 = [[random.randint(-100, 100) for i in range(k)] for i in range(n)]
tmp2 = [[random.randint(-100, 100) for i in range(k)] for i in range(n)]
tmp3 = [] 

for i in range(len(tmp1)):
    r = []
    for j in range(len(tmp1[0])):
        r.append(tmp1[i][j] + tmp2[i][j])
    tmp3.append(r)

pl(tmp3)