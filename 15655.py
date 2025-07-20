n,m = map(int,input().split())
l = []
for i in map(int,input().split()):
    l.append(i)
l.sort()
ans = []

def recu(k):
    if len(ans) >= m:
        print(*ans)
        return
    for i in range(n):
        if l[i] == -1:
            continue
        if l[i] > k:
            ans.append(l[i])
            l[i] = -1
        recu(i)
        l[i] = ans.pop()
recu(0)