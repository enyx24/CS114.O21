Ax, Ay = [int(num) for num in input().split()]
Bx, By = [int(num) for num in input().split()]


def printPoint(x, y):
    print('('+str(x)+', '+str(y)+')', end = "")

def rotating(x, y):
    return [y, -x];

vAB = [Ax-Bx, Ay-By]
for i in range(4):
    printPoint(Ax, Ay)
    if (i != 3):
        print(' ', end = '')
    vAB = rotating(vAB[0], vAB[1])
    Ax += vAB[0]
    Ay += vAB[1]
print()

vAB = [Bx-Ax, By-Ay]
for i in range(4):
    printPoint(Ax, Ay)
    if (i != 3):
        print(' ', end = '')
    Ax += vAB[0]
    Ay += vAB[1]
    vAB = rotating(vAB[0], vAB[1])
#(2, 4) (2, 5) (3, 5) (3, 4)
#(2, 4) (3, 4) (3, 3) (2, 3)
#(2, 4) (2, 5) (3, 5) (3, 4)
#(2, 4) (3, 4) (3, 3) (2, 3)
#Bai` nay` bi. khung` ngay cai' cho la end line 1 k co' space.
