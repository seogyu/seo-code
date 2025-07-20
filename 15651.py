n,m = map(int,input().split())

l = [i for i in range(1,n+1)]
ans = []

def recu(k):
    if len(ans) >= m:
        print(*ans)
        return
    for i in range(n):
        ans.append(l[i])
        recu(k+1)
        l[i] = ans.pop()
recu(n)