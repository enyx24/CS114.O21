a = []
n = int(input())
a = [float(num) for num in input().split()]
x = int(input())
y = int(input())
z = float(input())
cnt = 0
dmg = 0

q = []
for i in range(n):
    q.append(a[i])
    dmg += x
    while (q[(0)] + z < a[i]):
        q.pop(0)
    dmg += (len(q)-1)*y

print(dmg)

