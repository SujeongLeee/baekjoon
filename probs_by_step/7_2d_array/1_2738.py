n, m = map(int, input().split())

matrices = []

for _ in range(2):
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    matrices.append(matrix)


for i in range(n):
    sum = [str(matrices[0][i][x] + matrices[1][i][x]) for x in range(m)]
    print(' '.join(sum))