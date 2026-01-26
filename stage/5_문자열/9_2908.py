a, b = input().split()
a = int(a[::-1]) # [::-1]: 문자열 뒤집기, 문자열로 받아야 뒤집을 수 있음.
b = int(b[::-1])
print(max(a,b))