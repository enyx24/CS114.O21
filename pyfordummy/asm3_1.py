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
a = []
a = [int(num) for num in input().decode().split()]
m = int(input())
d = {}
for num in input().decode().split():
    if num in d:
        ans = d[num]
    else:
        ans = binarySearch(a, int(num), lambda x, y: x <= y)
        d.update({num: ans})
    print(ans)
