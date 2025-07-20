n = int(input())
st = []
m = 0
for _ in range(n):
    k = int(input())
    if k == 0:
        st.pop()
    else:
        st.append(k)
for i in st:
    m+=i
print(m)