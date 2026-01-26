s = input().upper() # 대소문자 구분 안한댔으니까
unique = list(set(s)) # set: 문자열의 유니크한 알파벳
cnt = []

for i in unique:
    cnt.append(s.count(i)) # s안에 i가 몇개인지

maxcnt = max(cnt)

# 최빈값이 여러개인 경우
if cnt.count(maxcnt)>1:
    print('?')
else: # max(cnt) 가 cnt 에서 몇번째인지 출력하고 그 인덱스를 unique[]에 이용해서 알파벳 대문자로 출력
    idx = cnt.index(maxcnt) # .index: 위치 인덱스 알 수 있다.
    print(unique[idx])