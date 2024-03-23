import heapq, io, os, bisect
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

cmd = list(int(num) for num in input().decode().split())

l = []

while cmd[0] != 0:
    if (cmd[0] == 1):
        bisect.insort(l, cmd[1])
    else:
        if cmd[1] in l:
            print(1+l.index(cmd[1]))
        else:
            print(0)
    cmd = [int(num) for num in input().decode().split()]

