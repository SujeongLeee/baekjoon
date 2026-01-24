students = list(range(1, 30 + 1))

for _ in range(28):
    i = int(input())
    students[i - 1] = 0

for i in students:
    if i != 0:
        print(i)