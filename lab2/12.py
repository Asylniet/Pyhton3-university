a = str(input())
st = []
ok = False

for i in range(0, len(a)):
    if a[i] == '(' or a[i] == '{' or a[i] == '[':
        st.append(a[i])
    else:
        if len(st) == 0:
            print("No")
            ok = True
            break
        cur = a[i]
        last = st[-1]
        if (cur == '}' and last != '{') or (cur == ')' and last != '(') or (cur == ']' and last != '['):
            break
        st.pop()

if not ok:
    if len(st) == 0:
        print("Yes")
    else:
        print("No")

#open-closed