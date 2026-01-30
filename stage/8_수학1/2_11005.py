n,b = map(int, input().split())
result = ""

# 10진법을 b진법으로
while n>0:
    rest = n%b
    n = n//b
    if 0<= rest < 10: # A:10, ..., Z:35
        result += str(rest)
    else:
        result += chr(rest + ord('A') - 10)

print(result[::-1])