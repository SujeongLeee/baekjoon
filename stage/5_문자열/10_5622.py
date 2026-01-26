a = input()
alist = list(a) # 공백없이 split

# S, Z가 특이케이스
numlist = [] # ""는 문자 나열, []는 값 묶음 리스트

for i in range(len(alist)):
    diff = ord(alist[i])-ord('A')
    if diff == ord('S')-ord('A'):
        num = 7
    if diff > ord('S')-ord('A') and diff < ord('W')-ord('A'):
        num = 8
    if diff >= ord('W')-ord('A'):
        num = 9
    else:
        num = 2+diff//3
    
    numlist.append(num)

print(sum([x+1 for x in numlist]))
