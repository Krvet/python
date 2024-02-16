def bin(n):
    return n if n < 2 else str(bin(n // 2)) + str(n % 2)

def mult(k, j):
    return k * j

def degree(x, y):
    return x ** y

e = int(input(f'Введите число: '))
s = int(input(f'Введите число на которое умножаем: '))
t = int(input(f'Введите степень: '))

print(bin(e))
print(mult(e, s))
print(degree(e, t))