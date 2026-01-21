# 공넣기
N,M = map(int, input().split())
buckets = [0]*(N+1) # 0은 안쓰는 빈칸, 리스트
for _ in range(M): # 그냥 M개를 만든다. _는 반복 횟수 값은 안쓸거야 라는 관용적 표현
	i,j,k = map(int, input().split())
	for x in range(i,j+1): # range(a,b)는 b를 포함하지 않음
		buckets[x]=k # *: unpacking, list를 하나씩 꺼내서 print에 인자로 넣음
print(*buckets[1:])
