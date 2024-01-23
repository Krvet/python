n = set()

for i in input().split():
    if i not in n:
        n.add(i)
        print("No")
    else:
        print("Yes")
