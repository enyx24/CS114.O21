import math
r, c = [int(num) for num in input().split()]
a = []
for i in range(r):
    a.append([])
    a[i] = input().split()
t = []


for j in range(c):
    m = 0
    for i in range(r):
        a[i][j] = int(a[i][j])
        cnt = 0
        if a[i][j] != 0:
            if a[i][j] < 0:
                cnt = 1
            cnt += math.ceil(math.log10(abs(a[i][j])))
        else:
            cnt = 1
        m = max(m, cnt)
    t.append(m+ (1 if j > 0 else 0))

for i in range(r):
    for j in range(c):
        print(('{:>'+str(t[j])+'s}').format(str(a[i][j])), end = '')
    print()
