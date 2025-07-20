n = int(input())
st = []
t = []
for _ in range(n):
    t.append(int(input()))
idx = 0
ans = [] 
for i in range(1,n+1):
    st.append(i)
    ans.append("+")
    while st and st[-1] == t[idx]:
        st.pop()
        ans.append('-')
        idx+=1
if len(st) == 0:
    print(*ans , sep = '\n')
else:
    print('NO')