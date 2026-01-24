n, k = map(int, input().split())

factors = []

divider = 1

while divider <= n and len(factors) < k:
    if n % divider == 0:
        factors.append(divider)
    divider += 1

if len(factors) < k:
    print(0)
else:
    print(factors[k - 1])