n, m = map(int, input().split())

baskets = list(range(1, n + 1))

for _ in range(m):
    i, j = map(int, input().split())
    i -= 1 # match index
    j -= 1 # match index

    tmp_list = baskets.copy()
    for idx, k in enumerate(range(i, j + 1)):
        baskets[k] = tmp_list[j - idx]

print(' '.join(map(str, baskets)))