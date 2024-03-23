import heapq, io, os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
n, m = [int(num) for num in input().decode().split()]
heap = []
for i in range(n):
    heap.append(- int(input().decode().split()[0]))

heapq.heapify(heap)

for i in range(m):
    temp = [int(num) for num in input().decode().split()]
    com = temp[0]
    val = 0
    if (com <= -3):
        val = temp[1]
    if com == -1:
        if len(heap) == 0:
            continue
        heapq.heappop(heap)
    elif com == -2:
        if len(heap) == 0:
            continue
        t = heapq.heappop(heap)
        while len(heap) != 0 and heap[0] == t:
            heapq.heappop(heap)
    elif com == -3:
        if len(heap) == 0:
            continue
        heapq.heapreplace(heap, heap[0] + val)
    else:
        if len(heap) == 0:
            continue
        t = heap[0]
        while len(heap) != 0 and heap[0] == t:
            heapq.heapreplace(heap, heap[0] + val)

while len(heap) != 0:
    print(-heap[0])
    heapq.heappop(heap)
