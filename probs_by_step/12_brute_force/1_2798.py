n, m = map(int, input().split())

cards = list(map(int, input().split()))

result = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            if i == j or j == k or k == i:
                continue
            
            sum = cards[i] + cards[j] + cards[k]
            
            if sum > result and sum <= m:
                result = sum

print(result)