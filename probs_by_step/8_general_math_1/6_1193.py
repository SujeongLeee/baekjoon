x = int(input())

row = 1 # diagonal row

while x > row:
    x -= row
    row += 1

if row % 2 == 1:
    x = row - x + 1 # standardize direction

x -= 1 # match index

print(str(1 + x) + '/' + str(row - x))