# 분수찾기
x = int(input())

# 1
# 3 2
# 4 5 6
# 10 9 8 7
# 11 12 13 14 15

# (row, col)
# 4: shell 3, 오른쪽에서 3번째 => (3,1)
# 5: shell 3, 오른쪽에서 2번째 => (2,2)
# 6: shell 3, 오른쪽에서 1번째 => (1,3)
# 7: shell 4, 오른쪽에서 1번째 => (1,4)
# 11: shell 5, 오른쪽에서 5번째 => (5,1), -4 -> 5
# 12: shell 5, 오른쪽에서 4번째 => (4,2)
# 13: shell 5, 오른쪽에서 3번째 => (5,3), -2 -> 3
# 오른쪽에서 몇번째인지가 row
# shell - row +1 = col

# shell 마다 숫자 개수
# shell 1 = 1
# shell 2 = 2
# ...
# shell n = n

# find shell
xx = x
if xx == 1:
    print('1/1')
else:
    xx -=1
    shell = 2
    while True:
        xx -= shell
        if xx <= 0:
            if shell%2 == 0: # 짝수
                row = xx+shell
            else:
                row = -xx+1
            break
        shell += 1

    col = shell - row + 1
    print(str(row)+'/'+str(col))