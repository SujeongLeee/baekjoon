while True:
    n = int(input())
    if n == -1:
        break

    factors = []
    divider = 1
    while divider <= n /2:
        if n % divider == 0:
            factors.append(divider)
        divider += 1
    
    if sum(factors) == n:
        print(str(n) + ' = ' + ' + '.join(list(map(str, factors))))
    else:
        print(str(n) + ' is NOT perfect.')