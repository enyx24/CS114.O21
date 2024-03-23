import os, io
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

def binarySearch(a, x, comp, k):
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
t = input().decode().split()
k = int(t[0])
x = int(t[1])
pos = binarySearch(a, x, lambda x, y: x < y, k)
for num in a[pos: pos+k]:
    print(num, end = " ")