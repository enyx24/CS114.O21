import os, io
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

n, m = [int(num) for num in input().decode().split()]
a = [int(num) for num in input().decode().split()]
b = [int(num) for num in input().decode().split()]

a = set(a)
b = set(b)
print(len(a.intersection(b)))


# cung` 1 code nay` submit id 143261 mle 1 test id 143370 acp???
