import os, io
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
inp = (input().decode())
n = int(inp)
a = [None]*n

cnt = 0
for i in range(n):
    #input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
    a[i] = input().decode()
    #print(a[i])
    if i >= (n//2) and a[n-i-1] != a[i]:
        cnt += 1
    if cnt > 1:
        break
if cnt <= 1:
    print('TRUE')
else:
    print('FALSE')
