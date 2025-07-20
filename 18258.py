from collections import deque
import sys
def input():
    return sys.stdin.readline().rstrip()
q = deque()
n = int(input())
for _ in range(n):
    l = input().split()
    if l[0] == 'push':
        q.append(l[1])
    elif l[0] == 'size':
        print(len(q))
    elif l[0] == 'pop':
        if len(q) !=0:
            print(q.popleft())
        else:
            print(-1)
    elif l[0] == 'empty':
        if len(l) == 0:
            print(1)
        else:
            print(0)
    elif l[0] == 'front':
        if len(q) != 0:
            print(q[0])
        else:
            print(-1)
    else:
        if len(q) != 0:
            print(q[-1])
        else:
            print(-1)