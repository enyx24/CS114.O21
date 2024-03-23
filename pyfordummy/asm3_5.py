import os, io, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

def binarySearch(a, x, k):
    l = 0
    r = len(a)-k
    ans = -1
    while (l < r):
        m = l + (r-l)//2
        if x < a[m]:
            r = m
        elif a[m+k] <= x:
            l = m+1
        else:
            middist = abs(x-a[m])
            midkdist = abs(x-a[m+k])
            if middist <= midkdist:
                r = m
            else:
                l = m+1
    return l

input()
a = [int(num) for num in input().decode().split()]
while 1:
    try:
        t = input().decode().split()
        if len(t) == 0:
            break
        k = int(t[0])
        x = int(t[1])
        pos = binarySearch(a, x, k)
        print(a[pos], a[pos+k-1])
    except EOFError:
        break
