# 공넣기
N,M = map(int, input().split())
buckets = [0]*(N+1)
for _ in range(M):
	i,j,k = map(int, input().split())
	for x in range(i,j+1):
		buckets[x]=k
print(*buckets[1:])
