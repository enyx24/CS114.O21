import math
l, r = [ int(num) for num in input().split()]

def eratos(x):
    ans = []
    chk = []
    chk.extend([True]*(x))
    for i in range(2, x):
        if (chk[i] == True):
            for j in range(2,x//i):
                chk[i*j] = False
            ans.append(i)
    return ans

def primeFactors(n, primeList):
    i = 0
    factors = []
    while primeList[i]*primeList[i] <= n:
        if n % primeList[i]:
            i += 1
        else:
            n //= primeList[i]
            factors.append(primeList[i])
    if n > 1:
        factors.append(n)
    return factors

a = []
primeList = eratos(int(math.sqrt(r))+2)

for i in range (l, r+1):
    temp = primeFactors(i, primeList)
    temps = set(temp)
    if len(temp) == len(temps):
        a.append(temps)
cnt = 0
for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if len(a[i].intersection(a[j])) == 0:
            cnt += 1
print(cnt)

