# 나머지
rest = [0]*10
for i in list(range(1,11)):
    n = int(input())
    rest[i] = n%42

print(len(set(rest))) # 파이썬에서는 중복 제거가 set
