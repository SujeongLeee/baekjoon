n = int(input())

divider = 2
prime_factors = []

while n > 1:
    if n % divider == 0:
        prime_factors.append(divider)
        n /= divider
    else:
        divider += 1

for i in prime_factors:
    print(i)