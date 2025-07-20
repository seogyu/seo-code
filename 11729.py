n = int(input())
ans = []
def recu(start , mid , end , n):
    if n == 1:
        ans.append((start , end))
        return
    recu(start , end , mid , n-1)
    ans.append((start,end))
    recu(mid,start,end,n-1)
recu(1,2,3,n)
print(len(ans))
for i in ans:
    print(*i)