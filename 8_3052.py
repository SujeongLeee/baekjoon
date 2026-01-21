# 나머지
rest = [0]*10
for i in range(1,11):
    n = int(input())
    rest[i] = n%42

print(unique(rest))