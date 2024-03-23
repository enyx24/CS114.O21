import os, io
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

def binarySearch(a, x, comp):
    l = 0
    r = len(a)-1
    ans = -1
    while (l <= r):
        m = (l+r)//2
        if (a[m] == x):
            ans = m
        if comp(a[m], x):
            l = m+1
        else:
            r = m-1
    return ans

n = int(input().decode())
a = {}
t = input().decode()
for i in range(n):
    x = t.find(' ')
    a.update({int(t[:x]): i})
    t = t[x+1:]
m = int(input())
for num in input().decode().split():
    if int(num) in a:
        print(a[int(num)])
    else:
        print(-1)
