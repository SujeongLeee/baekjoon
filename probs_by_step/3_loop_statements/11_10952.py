not_terminated = True

while not_terminated:
    a, b = map(int, input().split())
    if a == 0 & b == 0:
        not_terminated = False
        break
    print(a + b)