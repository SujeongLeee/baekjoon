# 나머지
rest = []
for _ in range(10):
    n = int(input())
    rest.append(n%42)

print(len(set(rest))) # 파이썬에서는 중복 제거가 set
