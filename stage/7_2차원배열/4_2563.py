n = int(input())
l = []
b = []

for _ in range(n):
    ldist, bdist = map(int, input().split())
    l.append(ldist)
    b.append(bdist)

# 둘중 하나라도 차이가 10 이상이면 안겹치고
# 둘다 10 이하면 겹친다.


# print(l)
# print(b)
# entire = (10**2)*3
# overlap = 