import math
n = int(input())

def check(a, b):
    if len(a) != len(b):
        return False
    dicta = {}
    for i in range(len(a)):
        dicta[a[i]] = []
    for i in range(len(a)):
        dicta[a[i]].append(i)

    for j in range(len(b)):
        flag = False
        if b[j] not in dicta:
            return False
        for i in dicta[b[j]]:
            if abs(i-j+1)%2 == 1:
                dicta[b[j]].remove(i)
                flag = True
                break
        if flag == False:
            return False
    return True

while (n > 0):
    a = input()
    b = input()
    if check(a, b):
        print('YES')
    else:
        print('NO')
    n -= 1

# Do dai le -> a[i] == b[j] && (i-j)%2 == 1
# String khong gioi han do dai -> brute force
