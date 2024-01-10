m = int(input())
n = int(input())
Ai = []

for i in range(n):
    Ai.append(int(input()))

print((2 * min(Ai) <= m) + len([x for x in Ai if x + min(Ai) > m]))

        