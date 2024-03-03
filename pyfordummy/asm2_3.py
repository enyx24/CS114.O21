# from math import ceil, log10
import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
r, c = [int(num) for num in input().decode().split()]
a = []
for i in range(r):
    #inp = input().decode().split()
    #print(i.np)
    a += [input().decode().split()]
#print(a)
t = []


for j in range(c):
    m = 0
    for i in range(r):
        a[i][j] = int(a[i][j])
        cnt = 0
        if (a[i][j]) == 0:
            cnt = 1
        else:
            cnt += len(str(a[i][j]))
        m = m if m > cnt else cnt
    t+= [(m+ (1 if j > 0 else 0))]

for i in range(r):
    s = ""
    for j in range(c):
        s += (('%'+str(t[j])+'s') % ((a[i][j])))
    sys.stdout.write(s+'\n')
