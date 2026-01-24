n, b = input().split()
b = int(b)

sum = 0

for digit, num in enumerate(n[::-1]):
    try:
        sum += int(num) * (b ** digit)
    except:
        sum += (ord(num) - 55) * (b ** digit)

print(sum)