n, m = map(int, input().split())

baskets = []

for _ in range(n):
    baskets.append(0)

for _ in range(m):
    i, j, k = map(int, input().split())
    for l in range(i, j + 1):
        baskets[l - 1] = k

output = str()
for i in baskets:
    output += f"{i} "
output = output[:-1]

print(output)