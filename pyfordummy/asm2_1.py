r, c = [int(num) for num in input().split()]
a = []
for i in range(r):
    a.append([])
    a[i] = [int(num) for num in input().split()]
b = a

cw = [[0, 1], [1, 0], [0, -1], [-1, 0]]
ccw = [[-1, 0], [0, -1], [1, 0], [0, 1]]


