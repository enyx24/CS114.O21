h, w, k = [int (num) for num in input().split()]
arr = []
for i in range(h):
    arr.append([])
    arr[i] = list(input())

def getBit(num, i):
    return (num >> i) & 1

def countBlack(arr, h, w, rState, cState):
    cnt = 0
    for i in range(h):
        for j in range(w):
            if getBit(rState, i) == 0 and getBit(cState, j) == 0 and arr[i][j] == '#':
                cnt += 1
    return cnt

def stateIteration(arr, h, w, k):
    cnt = 0
    for i in range(2**h):
        for j in range(2**w):
            if countBlack(arr, h, w, i, j) == k:
                cnt += 1
    return cnt

print(stateIteration(arr, h, w, k))
