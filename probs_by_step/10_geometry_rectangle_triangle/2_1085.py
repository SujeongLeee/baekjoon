x, y, w, h = map(int, input().split())

distances = [
    x,
    y,
    abs(x - w),
    abs(y - h)
]

print(min(distances))