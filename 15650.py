n,m = map(int,input().split())

l = [i for i in range(1,n+1)]
ans = []

def recu(k):
    if len(ans) >= m:
        print(*ans)
        return
    for i in range(k,n):
        if l[i] == -1:
            continue
        ans.append(l[i])
        l[i]=-1
        recu(i+1)
        l[i] = ans.pop()
recu(0)