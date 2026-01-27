n = int(input())
pair = []

for _ in range(n):
    ldist, bdist = map(int, input().split())
    pair.append([ldist, bdist])

overlap = 0
for i in range(n-1):
    # print('i:',i)
    for j in range(1,n-i):
        # print('j:',j)
        l = abs(pair[i][0]-pair[i+j][0])
        r = abs(pair[i][1]-pair[i+j][1])
        if l>= 10 or r >= 10: 
            overlap += 0
        else:
            ll = abs(pair[i][0]+10 - pair[i+j][0])
            rr = abs(pair[i+j][1]+10 - pair[i][1])
            overlap += ll*rr

# print(overlap)
print((10**2)*3-overlap)

# 어떤 영역이 여러번 겹치는 경우에는 ???????