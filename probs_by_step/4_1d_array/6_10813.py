n, m = map(int, input().split())

baskets = list(range(1, n + 1))

for _ in range(m):
    i, j = map(int, input().split())

    i_prev = baskets[i - 1]
    j_prev = baskets[j - 1]

    baskets[i - 1] = j_prev
    baskets[j - 1] = i_prev

print(' '.join(map(str, baskets)))