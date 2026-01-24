n, b = map(int, input().split())

terminated = False
digits = list()

while not terminated:
    digits.append(int((n % (b ** (len(digits) + 1))) / (b ** len(digits))))
    n -= digits[-1] * (b ** (len(digits) - 1))
    if n <= 0:
        terminated = True

for digit in digits[::-1]:
    if digit < 10:
        print(digit, end = '')
    else:
        print(chr(digit + 55), end = '')