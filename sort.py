list = [5, 3, 7, 3, 1]
s = len(list)

for i in range(s-1):
    sorted = True
    for j in range(0, s - 1 - i):
        if list[j] > list[j + 1]:
            list[j], list[j + 1] = list[j + 1], list[j]
            print(f'начало {list}')
            sorted = False
    if sorted:
        break

print(list)



