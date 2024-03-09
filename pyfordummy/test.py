import sys

def stdin_gen():
    for x in sys.stdin.read().split():
        yield int(x)
def get_ints(): 
    return list(map(int, sys.stdin.readline().strip().split()))


#print(cin)
n = get_ints()
a = get_ints()
print(n)
print(a)
