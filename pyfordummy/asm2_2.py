r = int(input().split()[0])
t = []
for i in range(r):
    t.append([])
    t[i] = [int(num) for num in input().split()]
t = t[::-1]
for i in range(r):
    for j in t[i]:
        print(j, end = ' ')
    print()
