mat = []
maxs = []
for _ in range(9):
    row = list(map(int, input().split()))
    mat.append(row)
    maxs.append(max(row))

# 최댓값이 두 개 이상인 경우 그 중 한 곳의 위치를 출력한다.
maxmax = max(maxs)
rowidx = maxs.index(maxmax)
colidx = mat[rowidx].index(maxmax)

print(maxmax)
print(rowidx+1, colidx+1)