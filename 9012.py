n = int(input())
l = []
for _ in range(n):
    m = input()
    st = []
    for c in m:
        if c=="(":
            st.append(c)
        elif c== ")":
            if len(st) == 0:
                st.append(0)
                break
            else:
                st.pop(0)
    if len(st) == 0:
        print('YES')
    else:
        print('NO')