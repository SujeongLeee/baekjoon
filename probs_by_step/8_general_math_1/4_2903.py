n = int(input())

dots = 2

for _ in range(n):
    dots = dots * 2 - 1

print(dots * dots)