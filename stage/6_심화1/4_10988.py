# sol1
s = input()
slist = list(s)
slen = len(slist)
# print(slist); print(slen)
if slen%2==0:
    idx = int(slen/2)
    left = slist[0:idx] # 여기는 0부터 끝까지 다 포함
    right = slist[idx:slen][::-1] # 여기는 처음+1 부터 끝까지 포함 ?????
    # print(left); print(right)
    if left==right:
        print(1)
    else:
        print(0)
else:
    idx = int((slen-1)/2)
    left = slist[0:idx] # 여기는 0부터 끝까지 다 포함
    right = slist[idx+1:slen][::-1] # 여기는 처음+1 부터 끝까지 포함 ?????
    # print(left); print(right)
    if left==right:
        print(1)
    else:
        print(0)