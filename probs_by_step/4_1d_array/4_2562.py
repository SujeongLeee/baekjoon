array = []
for _ in range(9):
    array.append(int(input()))

max = max(array)
idx = array.index(max) + 1

print(max, idx)