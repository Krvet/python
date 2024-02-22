import random

n = 1000
arr = list()
for i in range(n):
    number = random.randint(1, 100)
    arr.append(number)
ans = -1
to_search = random.randint(1, 100)

arr.sort()
left = 0
right = len(arr) - 1
while (left <= right) and (to_search >= arr[left]) and (to_search <= arr[right]):
    p1 = float(right - left) / (arr[right] - arr[left])
    p2 = to_search - arr[left]
    index = left + int(p1 * p2)

    if arr[index] == to_search:
        ans = index
        break
    if arr[index] < to_search:
        left = index + 1
    else:
        right = index - 1

print(arr)
print(to_search)

if ans != -1:
    print(f'Элемент в списке, его индекс: {ans}')
else:
    print('Элемента нет')