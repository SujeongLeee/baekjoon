n = int(input())

coords = []

for _ in range(n):
    coords.append(tuple(map(int, input().split())))

coords_x = [x[0] for x in coords]
coords_y = [x[1] for x in coords]

width = max(coords_x) - min(coords_x)
height = max(coords_y) - min(coords_y)

print(width * height)