# 과제 안 내신 분..?
numbers = list(range(1,31))
for _ in range(28):
    n = int(input())
    if n in numbers:
        numbers.remove(n) # numbers에서 n 과 똑같은거 찾아서 제거

print(min(*numbers))
print(max(*numbers))