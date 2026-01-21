# 평균
n = int(input())
scores = list(map(int, input().split())) # 점수가 n만큼

m = max(scores)

newscores = []
for s in scores:
    newscores.append(s/m*100)

print(sum(newscores)/n)