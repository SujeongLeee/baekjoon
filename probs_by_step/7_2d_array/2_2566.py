matrix = list()

for _ in range(9):
    matrix.append(list(map(int, input().split())))

max_val = -1
max_pos = [1, 1]

for idx, row in enumerate(matrix):
    if max(row) > max_val:
        max_val = max(row)
        max_pos = [idx + 1, row.index(max_val) + 1]

print(max_val)
print(max_pos[0], max_pos[1])