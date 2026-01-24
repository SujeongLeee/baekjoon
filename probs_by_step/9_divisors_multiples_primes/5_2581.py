def is_prime(n):
    if n == 1:
        return False
    divider = 2

    while divider <= n / 2:
        if n % divider == 0:
            return False
        divider += 1
    else:
        return True

m = int(input())
n = int(input())

primes = []

for i in range(m, n + 1):
    if is_prime(i):
        primes.append(i)

if len(primes) == 0:
    print(-1)
else:
    print(sum(primes))
    print(min(primes))