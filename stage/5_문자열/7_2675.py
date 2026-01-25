# sol1
t = int(input())
for _ in range(t):
    rs = str(input())
    r = int(rs[0])
    s = rs[2:]
    for i in range(len(s)):
        print(s[i]*r, end="")
    

