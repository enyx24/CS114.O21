import math
n = int(input())
cnt = 0
for i in range(1, math.ceil(math.sqrt(n*n//2))+1):
    temp = math.sqrt(n*n-i*i)
    if int(temp) == temp:
        cnt += 1
        print(i, temp)
print(cnt)
