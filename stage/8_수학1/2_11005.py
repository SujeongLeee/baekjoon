n,b = map(int, input().split())

r = ""
a = n
while a>0:
    rest = n%b # 나머지
    a = n%b
    r+=str(rest)
    n = a//b
    
print(r)
