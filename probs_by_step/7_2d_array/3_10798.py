matrix = list()

for _ in range(5):
    matrix.append([x for x in input()])

for col in range(15):
    for row in range(5):
        try:
            print(matrix[row][col], end = '')
        except:
            pass