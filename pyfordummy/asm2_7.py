i, m = [int(num) for num in input().split()]
l = []
r = []
i *= 100
for j in range(m):
    t = input().split()
    if (t[1] == 'left'):
        l.append(int(t[0]))
    else:
        r.append(int(t[0]))
turn = 1
li = 0
ri = 0
cnt = 0
#print(i)
while li + ri < m:
    cap = i
    if (turn == 1):
        while li < len(l) and cap >= l[li]:
            cap -= l[li]
            li += 1
    else:
        while ri < len(r) and cap >= r[ri]:
            cap -= r[ri]
            ri += 1
    #print(li, ri)
    turn *= -1
    cnt += 1
print(cnt)
