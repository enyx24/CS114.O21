n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

amin = min(a)
amax = max(a)

print((amax - amin + 1) - n)
