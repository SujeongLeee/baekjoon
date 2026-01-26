s = input()
cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

cnt = 0
i = 0

# 문자를 누적해서 탐색
while i < len(s): # while 뒤의 조건을 만족하면 계속 돌려라 / 문자열은 len으로 길이를 잴 수 있다.
    if s[i:i+3]=='dz=':
        cnt += 1
        i += 3
    elif s[i:i+2] in cro:
        cnt += 1
        i += 2
    else:
        cnt += 1
        i += 1

print(cnt)