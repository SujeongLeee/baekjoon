# 진법변환
n,b = input().split()
b = int(b)

num = 0
for i, char in enumerate(reversed(n)): # reversed 를 사용한 건 list(n)을 안했기 때문?
    if '0' <= char < '10': # 한번에 비교 가능..
        digit = int(char)
    else:
        digit = (ord(char)-ord('A')+10)
    num += digit*(b**i)

print(num)