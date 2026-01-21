# 바구니 뒤집기
n,m = map(int, input().split())
baskets = list(range(1,n+1))
for _ in range(m):
    i,j = map(int, input().split())
    baskets[i:j] = baskets[j:i]
print(baskets)