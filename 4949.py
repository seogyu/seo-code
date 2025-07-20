while True:
    s = input()
    if s == '.':
        break
    st = []

    for i in s:
        if i == "(" or i=="[":
            st.append(i)
        elif i == ")":
            if len(st) !=0:
                if st[-1] == "(":
                    st.pop()
                else:
                    break
            else:
                st.append('c')
                break
        elif i == "]":
            if len(st) !=0:
                if st[-1] == "[":
                    st.pop()
                else:
                    break
            else:
                st.append('c')
                break
    if len(st) == 0:
        print('yes')
    else:
        print('no')