# 구슬탈출2
n,m = map(int, input().split()) # n: 세로, m: 가로
mat = []
for _ in range(n):
    row = input()
    mat.append(list(row)) ### 리스트로 바꿔줘야 '문자' -> '문','자'로 바뀜

# print(mat)

# where_hole, R, B
where_hole = []
where_R = []
where_B = []

for i in range(n):
    for j in range(m):
        if mat[i][j]=='O':
            where_hole = [i,j]
        elif mat[i][j]=='R':
            where_R = [i,j]
        elif mat[i][j]=='B':
            where_B = [i,j]

move_count = 0
ntrial = 10
directions = [[1,0], [-1,0], [0,-1], [0,1]] # 상하좌우

for _ in range(ntrial):
    R_goal = B_goal = False

    for direction in directions: # 모든 방향에 대해
        dy, dx = direction
        prev_R = where_R.copy()
        prev_B = where_B.copy()

        # 벽이나 다른 문자를 만날때까지 이동, 만나면 멈춤, 가다가 0 있어도 들어가야함
        while mat[where_R[0]+dy][where_R[1]+dx] not in ['#', 'B']:
            where_R[0] += dy
            where_R[1] += dx
            if where_R == where_hole:
                R_goal = True
                break
            else:
                mat[prev_R[0]][prev_R[1]]='.'
                mat[where_R[0]][where_R[1]]='R'
        
        
        # A, B는 독립적으로 움직이므로
        while mat[where_B[0]+dy][where_B[1]+dx] not in ['#', 'R']:
            where_B[0] += dy
            where_B[1] += dx
            if where_B == where_hole:
                B_goal = True
                break
            else:
                mat[prev_B[0]][prev_B[1]]='.'
                mat[where_B[0]][where_B[1]]='B'

        if prev_R != where_R or prev_B != where_B:
            move_count += 1
            break # 한번 이동하면 다른 방향은 다음 카운트에서 세야함

    if R_goal==True and B_goal==False:
        print(move_count)
        exit() # 즉시종료

    if R_goal==False and B_goal==True:
        print(-1)
        exit()

# ntrial 안에 못풀면 실패
print(-1)