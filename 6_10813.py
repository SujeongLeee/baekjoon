# 공바꾸기
N, M = map(int, input().split())
basket = [0]*(N+1)
for _ in range(M):
    i,j = map(int, input().split())
    ii = i*1
    jj = j*1
    basket[i] = jj
    basket[j] = ii
print(*basket[1:])
