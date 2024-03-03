hor = [0, 1, -1, 0]
ver = [1, 0, 0, -1]
def inp():
    try:
        uin = input()
    except EOFError:
        quit()
    r, c = [int(num) for num in uin.split()]
    a = []
    for i in range(r):
        a.append([1 if char == '-' else 0 for char in input()])
    return r, c, a

def flood(i, j, a, r, c):
    a[i][j] = 0
    for k in range(4):
        if i+hor[k] < 0 or i+hor[k] >= r or j+ver[k] < 0 or j+ver[k] >= c:
            continue
        elif a[i+hor[k]][j+ver[k]] == 1:
            flood(i+hor[k], j+ver[k], a, r, c)
    return


def solve(r, c, a):
    cnt = 0
    for i in range(r):
        for j in range(c):
            if a[i][j] == 1:
                cnt += 1
                flood(i, j, a, r, c)
    return cnt

cnt = 0
while (1):
    cnt += 1
    r, c, a = inp()
    print('Case ' + str(cnt) + ': ' + str(solve(r, c, a)))

