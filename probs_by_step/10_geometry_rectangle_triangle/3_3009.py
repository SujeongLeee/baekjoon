coords = []
for _ in range(3):
    coords.append(tuple(map(int, input().split())))

coords_x = sorted([x[0] for x in coords])
coords_y = sorted([x[1] for x in coords])

if coords_x[0] == coords_x[1]:
    coord_x = coords_x[2]
else:
    coord_x = coords_x[0]

if coords_y[0] == coords_y[1]:
    coord_y = coords_y[2]
else:
    coord_y = coords_y[0]

print(coord_x, coord_y)