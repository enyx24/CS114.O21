r, c = [int(num) for num in input().split()]
a = []
for i in range(r):
    a.append([])
    a[i] = [int(num) for num in input().split()]

def removeBorders(a, i):
    b = a
    first_row, last_column, last_row, first_column = [], [], [], []
    t = []
    if not any(b):
        return b
    if any(b):
        first_row = b.pop(0)
    if any(b):
        last_row = b.pop(-1)
    if any(b):
        last_column = [row.pop(-1) for row in b]
    if any(b):
        first_column = [row.pop(0) for row in b]
    b = removeBorders(b, i+1)

    if any(first_row):
        t += first_row
    if any(last_column):
        t += last_column
    if any(last_row):
        t += last_row[::-1]
    if any(first_column):
        t += first_column[::-1]

    if i%2 == 0:
        t = [t.pop(-1)]+t
    else:
        t = t+[t.pop(0)]
    c = max(len(first_row), len(last_row))
    r = max(len(first_column), len(last_column))
    first_row = t[:c]
    t = t[c:]
    last_column = t[:r]
    t = t[r:]
    last_row = t[:c]
    last_row = last_row[::-1]
    t = t[c:]
    first_column = t[::-1]
    #print(first_row, last_column, last_row, first_column)
    for i in range(r):
        if any(first_column):
            b[i].insert(0, first_column[i])
        if any(last_column):
            b[i].insert(len(b[i]), last_column[i])
    if any(first_row):
        b.insert(0, first_row)
    if any(last_row):
        b.insert(len(b), last_row)
    return b

t = removeBorders(a, 0)
for row in t:
    for val in row:
        print(val, end = " ")
    print()

