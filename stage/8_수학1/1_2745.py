# 진법변환
n,b = input().split()
b = int(b)

nlist = list(n)
num = 0

for i, char in enumerate(reversed(n)):
    # labeling
    if '0' <= char <= '9':
        digit = int(char)
    else:
        digit = ord(char)-ord('A')+10

    # result
    num += digit*(b**i)
print(num)
