# 공바꾸기
N, M = map(int, input().split())
basket = [0]*(N+1)
for _ in range(M):
    i,j = map(int, input().split())
    basket[i] = j
    basket[j] = i
print(*basket[1:])
